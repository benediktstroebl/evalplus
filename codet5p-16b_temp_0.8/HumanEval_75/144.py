
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    
    a = int(a)
    if a % 3!= 0:
        return False
    if a % 5!= 0:
        return False
    
    for i in range(2, a):
        if a % i == 0:
            if i % 3!= 0 and i % 5!= 0:
                return False
    return True

