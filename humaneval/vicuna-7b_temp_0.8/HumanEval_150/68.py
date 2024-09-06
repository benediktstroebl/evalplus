
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        if (n % 2) == 0:
            return y
        elif (n % 3) == 0:
            return x
        elif (n % 5) == 0:
            return y
        elif (n % 7) == 0:
            return x
        elif (n % 11) == 0:
            return y
        elif n > 11:
            for i in range(11, n):
                if (n % i) == 0:
                    return y
    else:
        return x

print(x_or_y(8, 123, 45)) # should return 45
print(x_or_y(11, 789, 34)) # should return 34

