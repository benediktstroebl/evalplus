
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        a_sqrt = a**0.5
        for i in range(2, int(a_sqrt)+1):
            if a % i == 0:
                # for all i such that a is divisible by i, check if i is prime
                if is_prime(i):
                    j = a/i
                    if is_prime(j):
                        if is_prime(a/j):
                            return True
        return False
    else:
        return False
    
