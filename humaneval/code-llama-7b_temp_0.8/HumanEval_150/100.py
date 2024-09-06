
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    #create a list of prime numbers
    prime_list = []
    #create a range from 1 to n+1
    for i in range (1, n+1):
        for j in range (2, n+1):
            if (i % j == 0 and i != j):
                break
        else:
            prime_list.append(i)
    #if n is in prime list return x otherwise return y
    if n in prime_list:
        return x
    else:
        return y
