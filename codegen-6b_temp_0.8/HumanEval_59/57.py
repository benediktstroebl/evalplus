

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    n = 2
    while n < n // 2:
        if n % 2 == 0:
            n += 2
            continue
        if n % 3 == 0:
            n += 6
            continue
        if n % 5 == 0:
            n += 20
            continue
        if n % 7 == 0:
            n += 21
            continue
        if n % 11 == 0:
            n += 37
            continue
        if n % 13 == 0:
            n += 41
            continue
        if n % 17 == 0:
            n += 49
            continue
        if n % 19 == 0:
            n += 61
            continue
        if n % 23 == 0:
            n += 71
            continue
        if n % 31 == 0:
            n += 83
            continue
        if n % 37 == 0:
            n += 97
            continue
        if n % 41 == 0:
            n += 113
            continue
        if n % 49 == 0:
            n += 127
            continue
        if n % 53 == 0:
            n += 131
            continue
        if n % 59 == 0:
            n += 137
            continue
        if n % 61 == 0:
            n += 139
            continue
        if n % 67 == 0:
            n += 149
            continue
        if n % 71 == 0:
            n += 157
            continue
        if n % 73 == 0:
            n += 163
            continue
        if n % 79 == 0:
            n += 167
            continue
        if n % 97 == 0:
            n += 173
            continue
        if n % 113 == 0:
            n += 177
            continue
        if n % 127 == 0:
            n += 199
            continue
        if n % 131 == 0:
            n += 211
            continue
        if n % 137 == 0:
            n += 223
            continue
        if n % 139 == 0:
            n += 227
            continue
        if n % 149 == 0:
            n += 233
            continue
        if n % 157 == 0:
            n += 239
            continue
        if n % 163 == 0:
            n += 251
            continue
        if n % 167