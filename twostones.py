stone=int(input())
if(stone>0 and stone<=(pow(10,7))):
    if(stone%2==0):
        print("Bob")
    else:
        print("Alice")