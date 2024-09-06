
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 3:
        return False
    prime_factors = []
    for i in range(2, int(a**0.5)):
        if a % i == 0:
            for prime in prime_factors:
                if i % prime == 0:
                    break
            else:
                prime_factors.append(i)
    if len(prime_factors) == 3:
        return True
    else:
        return False
