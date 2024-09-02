
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    import numpy as np
    x=np.array(x)
    y=np.array(y)
    n=np.array(n)
    if n>1:
        for i in n:
            if (i<=0):
                return print("n must be a positive integer")
            elif (i>0):
                for i in n:
                    if (n%i)==0:
                        print("n is a prime number")
                        return x
                    else:
                        print("n is not a prime number")
                        return y
    else:
        return print("n must be greater than 1")

