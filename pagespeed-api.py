import requests
import json

# Docs: https://developers.google.com/speed/docs/insights/v5/get-started

with open('pagespeed.txt') as pagespeedurls:
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    for line in content:
        file = open('pagespeed-results.csv', 'a')
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}'
        r = requests.get(x)
        final = r.json()
        urlid = final['id']
        ID = urlid
        urlfcp = final['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']
        FCP = f'First Contentful Paint: {urlfcp}'
        file.write(ID + '\n')
        file.write(FCP + '\n')

        #print(ID) Uncomment to test success
        #print(FCP) Uncomment to test success
