from cloudant.client import Cloudant

#authenticate using an IAM API key

client = Cloudant.iam('08bcbaf0-260b-48e0-abdb-08db348afcf2-bluemix','yhZfUubpS3vS1vEKZSS37teD6IAUi8oLynOCQLIwnQsa',connect=True)

#create  a database using an intitlized client

my_database = client.create_database('my_database')