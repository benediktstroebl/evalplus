

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    largest_prime_factor = 1
    prime_list = [2]
    for i in range(2, n + 1):
        prime_list.append(i)

    for i in range(len(prime_list)):
        if n % prime_list[i] == 0:
            n /= prime_list[i]
            break
        if (i == len(prime_list) - 1) and (n > 1):
            return n

    return largest_prime_factor

