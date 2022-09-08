# Q1: What Would Python Display?
 
def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
         return 6 + 7 + c
    else:
         return 25

# You can check your answer by running the command on terminal.
xk(10, 10)      #________________
xk(10, 6)       #________________
xk(4, 6)        #________________
xk(0, 0)        #________________


# Q2: 
def how_big(x):
     if x > 10:
        print('huge')
     elif x > 5:
        return 'big'
     elif x > 0:
        print('small')
     else:
        print("nothin")

how_big(7)      #________________        
how_big(12)     #________________        
how_big(1)      #________________        
how_big(-1)     #________________        


True and 13     #________________
False or 0      #________________
not 10          #________________
not None        #________________
#True and 1 / 0  #________________
True or 1 / 0   #________________

True or 1 / 0 or False              #________________
1 and 3 and 6 and 10 and 15         #________________
0 or False or 2 or 1 / 0            #________________

# Q3:Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

# Q4: Sum digits
# Hint: Think about how can you get the last digit of any number using modulo operator %
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"    

# Q5: Double digit
# Write a function that takes in a number and determines if the digits contain two adjacent 8s.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"    

# check your answers using command: python3     