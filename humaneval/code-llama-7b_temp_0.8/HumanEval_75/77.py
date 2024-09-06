
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Find all the prime numbers up to sqrt(a)
    # Starting from 2, find the primes and get their product
    # If the product is equal to a, we are done.
    # If not, loop on the primes again
    # If there are less than 3 primes, return false
    # If there are 3 primes but their product is not equal to a, return false
    # return True
    primes = [2]
    candidate = 3
    while candidate < a:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate = candidate + 2
    if len(primes) < 3:
        return False
    prod = 1
    for prime in primes:
        prod = prod * prime
    if prod == a:
        return True
    return False


