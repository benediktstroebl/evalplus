

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # if n is a prime, it is already the largest prime factor
    if n > 1 and n % 2 == 0:
        return n
    
    # otherwise, keep track of the largest prime factor found so far and continue
    largest_prime = 1
    for num in range(3, int(n**0.5) + 1, 2):
        if num > largest_prime:
            largest_prime = num
        if largest_prime * largest_prime > n:
            break
    return largest_prime

print(largest_prime_factor(13195))  # should print 29
print(largest_prime_factor(2048))  # should print 2