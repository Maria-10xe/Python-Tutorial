x = 12
y = 2 

x , y = 10.5,25
print(type(x))

def square(x):
  return x*x

sq = square(2)
x = 10


def absolute(x):
    if x>0:
        return x
    elif x==0:
        return 0
    else:
        return -x

a= absolute(-5)

def fib(n):
    prev, curr = 0, 1
    k = 1
    while k<n:
            prev, curr = curr, prev+curr
            k+=1
    return curr    
a =fib(3)