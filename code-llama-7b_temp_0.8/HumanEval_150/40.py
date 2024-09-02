
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Declare a variable for the return value
    ret_val = ''

    # Use a for loop to determine if n is prime or not
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            ret_val = y
            break
    else:
        ret_val = x

    return ret_val
