
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        if n % 2 == 0:
            return y
        elif n % 3 == 0:
            return x
        elif n % 5 == 0:
            return y
        elif n % 7 == 0:
            return x
        elif n > 7:
            if n % 3 == 0:
                return y
            elif n % 5 == 0:
                return x
            elif n % 7 == 0:
                return y
            else:
                return x
    else:
        return y

n = int(input("Enter the number of n: "))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if n > 1:
    return x_or_y(n, x, y)
else:
    return y
