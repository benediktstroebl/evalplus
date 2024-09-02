
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    #Solution 1
    #divisor = 2
    #while divisor*divisor < a:
    #    if a%divisor == 0:
    #        return False
    #    else:
    #        divisor += 1
    #return True

    #Solution 2
    prime = [2, 3, 5, 7, 11, 13]

    for x in prime:
        if a % x == 0 and a / x != 1:
            return False
    return True
