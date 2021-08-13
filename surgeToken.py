import requests, colorama

#install these modules
#pip3 install requests
#pip3 install colorama

from colorama import Fore, Back, Style
colorama.init()

#===========  Add/modify only here =============================================
#Add your apiKey from bscscan.com (register in bscscan and create the apiKey)
API_KEY="HBPRARYA7XI4YF4BEKEY3Q9S1ZXYDUW26D"
#Add your total token
BNB=40172309
ETH=1000000
USD=1000000
#============================ End  =============================================

#Surge token address
SURGE_BNB="0xE1E1Aa58983F6b8eE8E4eCD206ceA6578F036c21"
SURGE_USD="0x14fee7d23233ac941add278c123989b86ea7e1ff"
SURGE_ETH="0x5B1d1BBDCc432213F83b15214B93Dc24D31855Ef"
#Binance peg token address
B_PEG_ETH="0x2170ed0880ac9a755fd29b2688956bd959f933f8"
B_PEG_USD="0xe9e7cea3dedca5984780bafc599bd69add087d56"

#bscscan returns string value without any decimal grrrrrrr. 
BNB_DECIMAL=5 
ETH_DECIMAL=7
USD_DECIMAL=10

def surgeTokenDetails(SURGE_ADDRESS,B_PEG_ADDRESS,TOKEN_DECIMAL,TOKEN_NAME,TOTAL_TOKENS):

    totalBNB     = ((requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+ B_PEG_ADDRESS +"&tag=latest&apikey="+ API_KEY)).json())['result'];    
    totalSupply  = ((requests.get("https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress="+ SURGE_ADDRESS +"&tag=latest&apikey="+ API_KEY)).json())['result'];
    bnbPrice     = ((requests.get("https://api.bscscan.com/api?module=stats&action=bnbprice&apikey="+ API_KEY)).json())['result']['ethusd'];

    totalBNB = totalBNB[0:TOKEN_DECIMAL]+"."+totalBNB[TOKEN_DECIMAL:];  #bscscan returns string without any decimal grrrrrrr. (Ugly way to change)
    SURGE_TOKEN_VALUE=(float(totalBNB)/float(totalSupply))*float(bnbPrice);
    print("==========================================================")
    print("Total BNB         ====>  "+totalBNB);
    print("Total Supply      ====>  "+totalSupply);
    print("BNB Price         ====>  "+bnbPrice);
    print(TOKEN_NAME+" Price    ====>  "+"%.16f" % float(SURGE_TOKEN_VALUE));
    print("==========================================================")
    print(Fore.LIGHTGREEN_EX + "You own "+ TOKEN_NAME +"  ====> $ {0}".format(float(SURGE_TOKEN_VALUE*TOTAL_TOKENS)) + Style.RESET_ALL);
    print("==========================================================")


surgeTokenDetails(SURGE_BNB,SURGE_BNB,BNB_DECIMAL,"SurgeBNB",float(BNB));

#===== Need Token Holdings for SURGE_USD & SURGE_ETH - need pro account in bscscan :( ====

#surgeTokenDetails(SURGE_ETH,B_PEG_ETH,ETH_DECIMAL,"SurgeETH",float(ETH));
#surgeTokenDetails(SURGE_USD,B_PEG_USD,USD_DECIMAL,"SurgeUSD",float(USD));



#Not used now
#ethTokenHolding  = ((requests.get("https://api.bscscan.com/api?module=account&action=addresstokenbalance&address="+ SURGE_ETH +"&page=1&offset=100&apikey="+ API_KEY)).json());
#print(ethTokenHolding);

#bnbPrice     = ((requests.get("https://api.bscscan.com/api?module=stats&action=bnbprice&apikey="+ API_KEY)).json())['result']['ethusd'];
#ethTotalSupply = ((requests.get("https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress="+ B_PEG_ETH +"&tag=latest&apikey="+ API_KEY)).json())['result'];
#ethTotalSupply = ethTotalSupply[0:7]+"."+ethTotalSupply[7:]; 
#print("eth price ===> $ {0}".format(float(ethTotalSupply)/float(bnbPrice)));

