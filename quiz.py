import json
# from bs4 import BeautifulSoup
print("Welcome to Quiz App\n")
import requests
from random import seed
from random import random
from urllib.parse import unquote_plus
n=input("Enter number of Questions You Want: ")

f=requests.get("https://opentdb.com/api.php?amount={}&type=multiple&encode=url3986".format(n)).text
n=int(n)
# f=open("api.json")
data = json.loads(f)
c=0
for i in range(n):
    k=0
    print(unquote_plus(data["results"][i]["question"]))
    a= round(random()*3)
    # print(a)
    for j in range(4):

        if(j==int(a)):
            print(str(j+1)+". "+unquote_plus(data["results"][i]['correct_answer']))
        else:
            print(str(j+1) + ". " + unquote_plus(data["results"][i]['incorrect_answers'][k]))
            k+=1

    ans= input("Enter Your Answer: ")
    print("Answer: {}".format(unquote_plus(data["results"][i]["correct_answer"])))
    print("\n")
    try:
        if int(ans)==int(a)+1:
            c+=1
            print("Correct Answer")
        else:
            print("Incorrect Answer")
    except:
        if ans.lower()==data["results"][i]["correct_answer"].lower():
            c+=1
            print("Correct Answer")
        else:
            print("Incorrect Answer")

print("Your Score is: {} out of {}.".format(c,n))
