
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    
    if (n==1): #If n is a prime number then return the value of x
        return x
    elif (n%2==0): #If n is not a prime number and is divisible by 2 then return the value of y
        return y
    else: #Else return the value of x
        return x




