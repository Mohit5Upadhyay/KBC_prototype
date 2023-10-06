# KBCgaming...

questions = [
    ["Capital of India ?","delhi","goa","tundla","firozabad","none", 1],
    ["Capital of UP?","delhi","tundla","mandi","lucknow","none", 4],
    ["Name of space agengy of india ?","isro","roscosmos","stralink","nasa","none", 1],
    ["which is indian singer ?","mika singh","roly","Js john","phloo smith","none", 1],
    ["1-lunar day is equal to how manys earth days  ?","1","0","14","4","none", 3],
    ["G-20 sumit organise in which country ?","USA","UK","INDIA","BRAZIL","none", 3],
    ["In which year NEP is introduced  ?","2013","2020","2021","2019","none", 2],
    ["Name the UK PM that is by religion - hindu ?","borish johnson","Rishi Sunak","Roosevelt","Henry smith","none", 2],
    ["Taj mahal is located at which place ?","Agra - india","Varansi - india","Sultanpur - india","naviMumbai - india","none", 1],
    ["Molecular weight of H2O is ?","18","20","24","34","none", 1]
    ]
    
levels = [1000,2000,3000,5000,10000,20000,40000,80000,16000,320000]
# i=0
money=0

head="\n\n W   E   L   C   O   M   E       TO         K    B   C - Prototype   "
print(head.center(80))

for i in range(len(questions)):
    question = questions[i]
    print(f" \n Q. {question[0]} ")
    print(f"\n Question for RS. {levels[i]} ")
    print(f"a. {question[1]}                                   b. {question[2]}")
    print(f"c. {question[3]}                                   d. {question[4]}")

    reply=int(input("Enter Your answer ( 1-4 ) or 0 to Quit  the Game "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply  == question[-1]):
        print(f"Correct ANSWER , you have Won Rs. {levels[i]}")
        if(i == 4):
            money=10000
        elif(i == 9):
            money=320000
        elif(i == 14):
            money=10000000
    else:
        print("wrong answer !")
        break

print(f"Your take home money is :- {money}")
