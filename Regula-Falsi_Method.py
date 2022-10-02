y = input('Enter a Non-Linear Equation : ')
def f(x):
    f = eval(y)
    return f

def falsi(x0,x1,e):
    step = 1
    condition = True
    while condition:
        x2 = x0-(x1-x0)*f(x0)/(f(x1)-f(x0))
        print('Iteration-%d,x2 = %0.6f and f(x2) = %0.6f' % (step,x2,f(x2)))

        if f(x0)*f(x2)<0:
            x1=x2
        else:
            x0=x2

        step = step + 1
        condition = abs(f(x2)) > e
    print('\nActual Root is: %0.8f' % x2)

x0 = input('First Root: ')
x1 = input('Second Root: ')
e = input('Tolerable Error: ')

x0 = float(x0)
x1 = float(x1)
e = float(e)
while f(x0)*f(x1)>0:
    x0=x0+1
    x1=x1+1

if f(x0)*f(x1)>0.0:
    print('Given Guess values do not bracket the root.')
    print('Try Again with different values.')
else:
    falsi(x0,x1,e)
