
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        primes = []
        for i in range(2, 100):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primes.append(i)
        for i in range(2, 10):
            for k in range(2, 10):
                for j in range(2, 10):
                    if i * k * j == a:
                        if i in primes and k in primes and j in primes:
                            return True
        return False
    else:
        return "Input is too big"
        
