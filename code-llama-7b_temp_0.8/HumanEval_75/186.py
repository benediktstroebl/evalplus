
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime = [2,3,5,7]
    if a==1:
        return False
    for x in prime:
        if a%x==0:
            for y in prime:
                if a%y==0:
                    for z in prime:
                        if a%z==0:
                            return True
    return False
