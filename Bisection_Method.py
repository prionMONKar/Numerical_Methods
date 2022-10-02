y=input('Enter a Non-Linear Equation : ')
def f(x):
    f = eval(y)
    return f
def bisection(a,b,e):
    while b-a>=e:
        c=(a+b)/2
        if f(c)*f(a)<0:
            b=c
        elif f(c)*f(a)>0:
            a=c
    print("Actual Root is:",c)
    c=(a+b)/2.0
a = float(input("Start Range,a: "))
b = float(input("End Range,b: "))
e = float(input("Tolerable Error,e: "))
while f(a)*f(b)>0:
    a=a+1
    b=b+1
if f(a)*f(b)>0:
    print("Change a and b.")
else:
    bisection(a,b,e)