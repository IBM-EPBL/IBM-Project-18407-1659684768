import requests
result = "1"
url = "https://www.fast2sms.com/dev/bulkV2"
querystring = {
    "authorization":"ucDxAe7hgIFqnOS5EQBdt4lYJmsX6pj2VPzka3wHZ0fNyU1b8iGfqYlXFceBIEDMAOo2UJhTV6PdWQns",
        "sender_id":"DR-PREDICTION",
        "message":"Results: "+ result,
        "language":"english",
        "route":"q",
        "numbers": "9361079005, 9445979800"
    }
headers = {
        'cache-control': "no-cache"
    }

    
print(querystring)
res = requests.request("GET",url,headers=headers,params=querystring)
print(res.text)