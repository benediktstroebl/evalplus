

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # last = n
    # while n % 2 == 0:
    #     n //= 2
    # if n == last:
    #     return last
    # last = n
    # while n % 3 == 0:
    #     n //= 3
    # if n == last:
    #     return last
    # while n % 5 == 0:
    #     n //= 5
    # if n == last:
    #     return last
    # while n % 7 == 0:
    #     n //= 7
    # if n == last:
    #     return last
    # while n % 11 == 0:
    #     n //= 11
    # if n == last:
    #     return last
    # while n % 13 == 0:
    #     n //= 13
    # if n == last:
    #     return last
    # while n % 17 == 0:
    #     n //= 17
    # if n == last:
    #     return last
    # while n % 19 == 0:
    #     n //= 19
    # if n == last:
    #     return last

    # any prime greater than 19 is of the form 6n-1 or 6n+1
    # in this case, we know that n is not a multiple of 2, 3, or 5, so we can mod by 6
    # loop while n is not a multiple of 6
    # if it is a multiple of 6, set n to (n/6)
    # divide by 2, divide by 3, divide by 5, divide by 11, divide by 13, divide by 17, divide by 19
    # if we can divide by 2, do it, else if we can divide by 3, do it, else if we can divide by 5, do it,
    # else if we can divide by 7, do it, else if we can divide by 11, do it, else if we can divide by 13, do it,
