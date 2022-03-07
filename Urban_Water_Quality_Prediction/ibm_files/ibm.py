import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "P8IHL_tzkzULnAclJoMrP6CtLRmGgpS3_bGCHEjOpFX6"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [['do', 'ph', 'co', 'bod', 'na', 'tc', 'year']], "values": [[6.7,7.5,203.0,6.940049,0.1,27.0,2014]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8713ec1e-7f68-49af-9378-90607e9dd867/predictions?version=2022-03-05', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
pred=response_scoring.json()
y_pred=pred['predictions'][0]['values'][0][0]
print(y_pred)