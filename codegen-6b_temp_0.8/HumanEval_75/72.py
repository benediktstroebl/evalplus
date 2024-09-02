
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2,3,5]
    for number in range(len(primes),a+1):
        if all([number%prime == 0 for prime in primes]):
            primes.append(number)
    return a in primes
