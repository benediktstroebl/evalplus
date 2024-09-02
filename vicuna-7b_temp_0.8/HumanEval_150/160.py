
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Convert n to an integer
    n = int(n)
    
    # Define x and y
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    
    # If n is prime, return x
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            return x
    
    # If n is not prime, return y
    else:
        return y
