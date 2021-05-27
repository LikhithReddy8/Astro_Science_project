11import dc
import pickle
import datetime
ls=[]
m=[]
def create():
    n=int(input("ENTER THE NUMBER OF TOKENS:"))
    for i in range(1,n+1):
        name=input("ENTER YOUR NAME")
        print("DD/MM/YY")
        d=list(map(int,input("ENTER THE DATE OF BIRTH BY SPACING:").split()))
        u=name.upper()
        if u not in ls and d not in m:
            m.append(d)
            ls.append(u)
        else:
            print("\nERROR")
    d=dict(zip(ls,m))
    with open("dict.pickle","wb") as f:
        pickle.dump(d,f)
    return
def append():
    n=int(input("\nENTER THE NUMBER OF NEW TOKENS:"))
    for i in range(1,n+1):
        name=input("ENTER YOUR NAME")
        print("DD/MM/YY")
        d=list(map(int,input("\nENTER THE DATE OF BIRTH BY SPACING").split()))
        u=name.upper()
        if u not in ls and d not in m:
            m.append(d)
            ls.append(u)
        else:
            print("\nERROR")
    d1=dict(zip(ls,m))
    with open("dict.pickle","rb") as f:
        d=pickle.load(f)
    d.update(d1)
    with open("dict.pickle","wb") as f:
        pickle.dump(d,f)
    return
def display():
    with open("dict.pickle","rb") as f:
        d=pickle.load(f)
    print(d)
    print(d.keys())
    print(d.values())
    return
def search():
    with open("dict.pickle","rb") as f:
        d=pickle.load(f)
    print(d)
    k=input("ENTER THE NAME:")
    k=k.upper()
    j=list(map(int,input("ENTER THE DOB BY SPACING:").split()))
    if k in d.keys():
        if(j==d[k]):
            z=k[0]
            x=j[0]
            y=j[1]
            age=2019-j[2]
            print("\n",k,"YOUR NOW ",age)
            dc.my_dob(x,y,k)
            dc.my_ch(z)
        
        else:
            print("\nYOUR DATA BIRTH IS NOT MATCHED:")
            print("\nTRY AGAIN LATER")
    else:
        print("YOUR NAME NOT FOUND")
    return
print("WELCOME TO WESTREN ASTROLOGY")
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
ch=1
while ch!=0:
    print("\n************MENU*******************")
    print("\n1.CREATE NEW FILE\n2.APPEND A NEW TOKEN\n3.DISPLAY\n4.SEARCH\n0.EXIT")
    ch=int(input("\nENTER THE CHOICE:"))
    if ch==1:
        create()
    elif ch==2:
        append()
    elif ch==3:
        display()
    elif ch==4:
        search()
    elif ch==0:
        print("EXITING!")
    else:
        print("INAVLID CHOICE")
        

            
        
