
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
        while primes_list:
            prime = primes_list.pop(0)
            if a % prime != 0:
                return False
            a /= prime
        return True
    return False

