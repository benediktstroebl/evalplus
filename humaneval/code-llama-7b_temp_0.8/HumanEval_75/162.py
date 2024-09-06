
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        primes = [x for x in range(2,a) if is_prime(x)]
        while len(primes) > 1:
            if a == 1:
                return False
            b = primes[0] * primes[1]
            if b == a:
                return True
            elif b < a:
                primes.pop(0)
            else:
                primes.pop(1)
    else:
        return False
