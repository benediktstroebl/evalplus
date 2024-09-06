

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    k = n
    while k % 2 == 0:
        k = k / 2
    while k % 3 == 0:
        k = k / 3
    while k % 5 == 0:
        k = k / 5
    while k % 7 == 0:
        k = k / 7
    while k % 11 == 0:
        k = k / 11
    while k % 13 == 0:
        k = k / 13
    while k % 17 == 0:
        k = k / 17
    while k % 19 == 0:
        k = k / 19
    while k % 23 == 0:
        k = k / 23
    while k % 29 == 0:
        k = k / 29
    while k % 31 == 0:
        k = k / 31
    while k % 37 == 0:
        k = k / 37
    while k % 41 == 0:
        k = k / 41
    while k % 43 == 0:
        k = k / 43
    while k % 47 == 0:
        k = k / 47
    while k % 53 == 0:
        k = k / 53
    while k % 59 == 0:
        k = k / 59
    while k % 61 == 0:
        k = k / 61
    while k % 67 == 0:
        k = k / 67
    while k % 71 == 0:
        k = k / 71
    while k % 73 == 0:
        k = k / 73
    while k % 79 == 0:
        k = k / 79
    while k % 83 == 0:
        k = k / 83
    while k % 89 == 0:
        k = k / 89
    while k % 97 == 0:
        k = k / 97
    return k
