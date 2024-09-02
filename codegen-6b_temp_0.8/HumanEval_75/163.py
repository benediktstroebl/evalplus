
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = a
    while n > 0:
        if is_prime(n):
            p = 2
            r = n % 10
            while p * p < n:
                if n % p == 0:
                    return False
                p += 1
            return n == r
        n //= 10
    return True
