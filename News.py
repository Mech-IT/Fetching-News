import requests
import json
r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR API KEY')
a=json.loads((r.text))

m="Good morning Pritam sir so our today's top news are as follows."
n="Thanks for listening if you need any help please remember me, have a good day"

def speakt(s):
   from win32com.client import Dispatch
   speak = Dispatch("SAPI.SpVoice")
   speak.Speak(s)

li=(a["articles"])
for i in range(1,(len(li)+1)):
   if i==1:
      print(m)
      speakt(m)
      speakt(f"news{i}")
      h=li[i-1]["title"]
      v=li[i-1]["url"]
      print(h)
      print(v)
      speakt(h)
      continue
   elif i==len(li):
      speakt(f"news{len(li)}")
      h = li[i-1]["title"]
      v = li[i-1]["url"]
      print(h)
      print(v)
      speakt(h)
      print(n)
      speakt(n)
      continue
   else:
      speakt(f"news{i}")
      h = li[i-1]["title"]
      v = li[i-1]["url"]
      print(h)
      print(v)
      speakt(h)
      continue









