
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    primes = [2]

    if n == 2:
        return x

    for i in range(3, n):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    
    if n in primes:
        return x
    return y
