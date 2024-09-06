

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    import math
    largest = 1
    
    while n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                n //= i
                if i > largest:
                    largest = i
                break
        else:
            n //= n
            if n > largest:
                largest = n
    return largest

