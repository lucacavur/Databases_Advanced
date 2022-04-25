import requests
from bs4 import BeautifulSoup
import logging
import time

#make the function
def get_values():

    logging.basicConfig(filename="values.txt", level=logging.INFO)

    #scrape the page
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    #get all the variables (they all have the same class, except the hash)
    rawVariables = soup.find_all('span', {'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
    hashVariables = soup.find_all('a', {'class': 'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})

    #make a list to store all the amountUSD-values
    amountUSD = []
    for value in rawVariables:
        if value.text[0] == "$":
            amountUSD.append(value.text[1:len(value.text)])

    #turn them into floats
    floats = []
    for value in amountUSD:
        value = value.replace(",", "")
        floats.append(float(value))

    #get highest value
    floats.sort()
    highest_value = floats[len(floats)-1]

    #Now find the highest "amountsUSD" value between all the values
    #first create a list with all the variables
    cleanVariables = []
    for variable in rawVariables:
        cleanVariables.append(variable.text)

    #find the index of "highest_value" within "cleanVariables"
    #within the clean_variables: ditch the "," used to seperate the thousands
    noComma = []
    for value in cleanVariables:
        value = value.replace(",","")
        noComma.append(value)

    #look for the index of the highest value
    indexHighestValue = -1
    for value in noComma:
        indexHighestValue+=1
        if value == "$"+str(highest_value):
            break


    #the hash that represents this index, has his own index
    indexHash = int(((indexHighestValue+1)/3)-1)

    #get the hash that represents this index
    highest_hash = hashVariables[indexHash].text

    #get the BTCvalue that within cleanVariables has the indexHighestvalue-1
    btcValue = cleanVariables[indexHighestValue-1]

    #get the time that within cleanVariables has the indexHighestvalue-2
    timestamp = cleanVariables[indexHighestValue-2]

    #get highest valueUSD
    valueUSD = "$"+str(highest_value)

    #log the values into a log.txt file
    logging.info("Hash value: "+ highest_hash)
    logging.info("BTC value: "+ btcValue)
    logging.info("USD value: "+ valueUSD)
    logging.info("Time: "+ timestamp)

while(True):
    get_values()
    time.sleep(60)

