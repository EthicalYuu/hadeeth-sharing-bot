import re, requests, json, http.client, time, schedule

# Posts to facebook page holds tokens, page_ID

def post_to_page(post):
    #Your Access Keys
    page_id_1 = 108475671531305
    facebook_access_token_1 = 'EAAGpLBJZAQEEBAErz9fZBSr5LUEvNDfHYWhaZAMw8Jd45X2kepgtfZCXBAfkR8BO6dCB6jBFORJQLjTkYSVEelRcXhATvnwg0qZApsjKnZAIeXxrWUmnuZATkhJeIzePidXWozcg1rZCJHZA1yvZAZA5HIxc1USXVpLa54FZBOyRCDZAsRQitIZBpAUZAJe'
    msg = post
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
    payload = {
    'message': msg,
    'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, data=payload)
    print(r.text)


# Used to remove html tags from string

CLEANR = re.compile('<.*?>')
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

# API requests to Sunnah.com

def gen_hadith():

    conn = http.client.HTTPSConnection("api.sunnah.com")

    payload = "{}"

    headers = { 'x-api-key': "SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk" }

    conn.request("GET", "/v1/hadiths/random", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    data = dict(data)
    eng_hadith = cleanhtml(data['hadith'][0]['body'])
    arab_hadith = cleanhtml(data['hadith'][1]['body'])
    return eng_hadith + '\n\n' + arab_hadith

def gen_post_to_page():
    post_to_page(gen_hadith())

def schedule_posts(time):
    schedule.every().day.at(time).do(gen_post_to_page)

schedule_posts('23:58')

while True:
    schedule.run_pending()
    time.sleep(1)


