

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    prime_list = [2, 3, 5, 7]
    i = 1
    while i <= n:
        if n % i == 0:
            prime_list.append(i)
            n = n / i
        else:
            i = i + 1
    return max(prime_list)

