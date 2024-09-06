

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: implement this function!

    prime_factor = 2
    #print(prime_factor)
    while n % prime_factor != 0:
        prime_factor += 1
    #print(prime_factor)
    if n == prime_factor:
        return prime_factor

    else:
        if prime_factor >= 2 and n % prime_factor == 0:
            while n % prime_factor == 0:
                n //= prime_factor
            return prime_factor
        else:
            return largest_prime_factor(n)
