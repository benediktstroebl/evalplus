
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    
    # write your code inside this box
    # remove "pass", insert your code and return the value of x or y
    prime = []
    for x in range(1, n+1):
        if n%x == 0:
            prime.append(x)
            
    if len(prime) == 2:
        return x
    else:
        return y

