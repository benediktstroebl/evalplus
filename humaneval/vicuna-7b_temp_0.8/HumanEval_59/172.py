

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        # find the first odd number greater than n
        i = (n + (len(str(n)) // 2) // 2) // 2
        if i % 2 == 0:
            break
        n = i
        
        # find the largest prime factor of n
        largest = 2
        for d in divisors(n):
            if n % d == 0:
                break
            if d > largest:
                largest = d
        if largest == 2:
            return 2
        else:
            return largest
