import sys
import subprocess
import urllib.request
import requests
import json
import webbrowser

#to get lang and loc via cmd
print("Enter language and fully qualified file name")
lang, prog = input().split()
#proc = subprocess.Popen([sys.executable, 'C:\\Users\\hp\\Documents\\Allocation.cpp'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc = subprocess.Popen([sys.executable, prog], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

proc.wait()
(stdout, stderr) = proc.communicate()

if stderr:
    var = stderr.decode(encoding='UTF-8', errors='strict')
    # print(stderr)
    ls = var.split("\n")

    param = ls[3].split(": ")
    print(param[0])
    print(param[1])

    att = {'tagged': lang, 'intitle': ls[3], 'order': "desc", 'sort': "activity", 'site': "stackoverflow"}
    data = urllib.parse.urlencode(att)
    req = "https://api.stackexchange.com/2.2/search" + '?' + data
    print(req)
    # r = urllib.request.urlopen(req)
    # charset = r.info().get_content_charset()
   
    try:
        r = requests.get(req)
    except requests.exceptions.RequestException as e:
        print("Error occured check connection")
        raise SystemExit(e)

    fdata = r.json()
    print(fdata)
    cnt = 0
    links = []
    for x in fdata["items"]:
        if (x["is_answered"] == True):
            cnt += 1
            links.append(x["link"])
            print(x["link"])
            if (cnt == 5):
                break

    for link in links:
        webbrowser.open_new_tab(link)

else:
   print(" No Error")
