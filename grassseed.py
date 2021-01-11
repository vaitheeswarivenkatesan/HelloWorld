c=float(input())
n=int(input())
t=0.0
for i in range(n):
    w,l=map(float,input().split())
    t=w*l+t
print(c*t)  