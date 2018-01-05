import requests
import simplejson as json

# Getting list of NCSSM Students FB group members
access_token = 'ABCDE' # removed for security
group_id = 12345 # removed for security

def getMembers(group_id, access_token):

    base = "https://graph.facebook.com/v2.9"
    node = "/" + group_id + "/members"
    parameters = "/?access_token=%s" % access_token + "/?limit=999"
    url = base + node + parameters

    response = requests.get(url)
    data = response.text

    return data

members_data = getMembers(group_id, access_token)
