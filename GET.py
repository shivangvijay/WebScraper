import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.javatpoint.com/cpp-mcq')
 
# check status code for response received
# success code - 200
# print(r.url)
 
# print content of request
# print(r.status_code)

 
# check status code for response received
# success code - 200
# print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

questions = []
optionA = []
optionB = []
optionC = []
optionD = []
Answer = []
Explanation = []

for a in soup.find_all("p","pq"):
    # print(a.contents[0])
    temp = a.contents[0]
    questions.append(temp)
    
  
for b in soup.find_all("ol","pointsa"):
    # print(b.contents[1].contents[0])
    temp = b.contents[1].contents[0]
    optionA.append(temp)
    # pass

optionA.append("0")

for b in soup.find_all("ol","pointsa"):
    # print(b.contents[3])
    temp = b.contents[3].contents[0]
    optionB.append(temp)
    # pass

optionB.append("0")

   
for b in soup.find_all("ol","pointsa"):
    # print(b.contents[5])
    temp = b.contents[5].contents[0]
    optionC.append(temp)
    # pass
   
optionC.append("0")


for b in soup.find_all("ol","pointsa"):
    # print(b.contents[7])
    temp = b.contents[7].contents[0]
    optionD.append(temp)
    # pass

optionD.append("0")

for i in soup.find_all("strong"):
    if i.contents[0] == "Answer:":
        temp = i.next_element.next_element
        Answer.append(temp)
        
for i in soup.find_all("strong"):
    if i.contents[0] == "Explanation:":
        temp = i.next_element.next_element
        Explanation.append(temp)

    
    
# print(len(Answer))


Set = {"Ques":questions , "OptionA": optionA, "OptionB": optionB, "OptionC": optionC, "OptionD": optionD, "Answer": Answer, "Explanation": Explanation}
# print(len(questions))
# print(len(optionA))
# print(len(optionB))
# print(len(optionC))
# print(len(optionD))

df = pd.DataFrame(Set)
df.to_excel("output.xlsx")



