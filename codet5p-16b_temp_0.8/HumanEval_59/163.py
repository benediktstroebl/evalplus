

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_num = n
    while n > 1:
        if n % 2 == 0:
            n = n/2
        elif n % 3 == 0:
            n = n/3
        elif n % 5 == 0:
            n = n/5
        elif n % 7 == 0:
            n = n/7
        else:
            n = n - 1
        print(max_num)
        if n < max_num:
            max_num = n
    return max_num

