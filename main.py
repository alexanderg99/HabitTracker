# This is a sample Python script.
import requests
import datetime

TOKEN = "dfwfqwrg334r"
ID = 'graph1'
USERNAME = 'alexg99'
headers = {
"X-USER-TOKEN":TOKEN

}

def formatdate():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    if len(month)<2:
        month = '0'+month
    day = str(datetime.datetime.now().day)
    if len(day)<2:
        day = '0'+day
    format = year+month+day

    return format



class HabitTracker(TOKEN, ID, USERNAME,headers):


    def __init__(self):
        self.TOKEN = TOKEN
        self.ID = ID
        self.USERNAME = USERNAME
        self.headers = headers

    def createNewAccount(self):
        params = {
            "token": TOKEN,
            "username": USERNAME,
            "agreeTermsOfService": 'yes',
            'notMinor': 'yes'

        }
        pixela_endpoint = 'https://pixe.la/v1/users'
        response = requests.post(url=pixela_endpoint,json=params)
        if response["isSuccess"] == 'true':
            print('Account Created')

    def createNewGraph(self):
        graph_configurations = {

            "id": ID,
            "name": "Greek Graph",
            "unit": "Minutes",
            "type": "int",
            "color": "ajisai"
        }
        graph_endpoint = 'https://pixe.la/v1/users/{}/graphs'.format(self.USERNAME)
        response = requests.post(url=graph_endpoint,json=graph_configurations, headers=self.headers)

        if response["isSuccess"] == 'true':
            print('Graph Created')

    def createPost(self):

        post_details = {
            'date': formatdate(),
            'quantity': '10'

        }

        post_endpoint = 'https://pixe.la/v1/users/{}/graphs/{}'.format(self.USERNAME, self.ID)

        response = requests.post(url=post_endpoint, json=post_details, headers=self.headers)













print(response.text)
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


