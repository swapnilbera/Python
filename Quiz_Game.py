qn=["1.What country has the highest life expectancy?\nA.HongKong B.Germany C.Canada D.India",
    "2.What year was the United Nations established?\nA.1945 B.1946 C.1947 D.1948",
    "3.Aureolin is a shade of what color?\nA.Yellow B.Red C.Green D.White",
    "4.The percentage of irrigated land in India is about?\nA.35 B.45 C.55 D.65",
    "5.With which sport is the Jules Rimet trophy associated?\nA.Football B.Cricket C.Hockey D.BasketBall"]
ans=["A","A","A","A","A"]
count=0
for i in range(len(qn)):
    print(qn[i])
    opt=input("Your option: ")
    if(opt==ans[i]):
        count+=1
        print("Your Ans is Correct!!!")
    else:
        count-=1
        print("Your ans is wrong....")
print("Your final amount is:$",count*100)


