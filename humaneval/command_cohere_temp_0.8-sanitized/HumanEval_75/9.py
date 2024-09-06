def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
    primes_sorted = sorted(primes)
    if len(primes_sorted) <= 3 * (a ** .5 + 1): 
        return False
    divisors = [num for num in primes_sorted[1:] if a % num == 0]
    return len(divisors) == 3