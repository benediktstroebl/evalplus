
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def prime_number(n):
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True
    
    i = 2
    while i * i <= a:
        if a % i == 0 and prime_number(i) and prime_number(a / i):
            return True
        i += 1
    return False
