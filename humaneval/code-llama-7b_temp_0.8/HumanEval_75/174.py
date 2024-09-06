
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        for i in range(2, a):
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
            if prime == True:
                a = a - i
                if a == 0:
                    return True
    return False
