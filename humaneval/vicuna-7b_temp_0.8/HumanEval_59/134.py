

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Handle the special case of 2 and handle the special case of 1
    if n == 2:
        return 2
    elif n == 1:
        return 1
    # Use a list to store the prime factors and their multiplicities
    prime_factors = []
    # Use a while loop to find the largest prime factor and multiply it by the next
    # highest power of 2 that is less than n
    i = 2
    while i * i <= n:
        # If the prime factor is not in the list or its multiplicity is greater than
        # the current highest multiplicity, add it to the list and update the highest
        # multiplicity
        if not prime_factors or prime_factors[-1][1] < i:
            prime_factors.append((i, 1))
            if n % i == 0:
                n //= i
                i = n // 2
            else:
                i += 1
        # If the prime factor is in the list and its multiplicity is greater than
        # the current highest multiplicity, update the highest multiplicity
        else:
            prime_factors[-1][1] = max(prime_factors[-1][1], i)
        # If the while loop completes, the largest prime factor is the last prime
        # factor in the list
    return max(prime_factors, key=lambda x: x[1])[0]
