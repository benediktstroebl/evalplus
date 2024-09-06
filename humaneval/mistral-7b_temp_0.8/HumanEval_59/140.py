

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # num = n
    # print(n)
    # while True:
    #     # if n%2 != 0:
    #     #     print(n)
    #     #     break
    #     n = n//2
    #     print(n)
    # return n

    i = 2
    while n > 1:
        while n%i == 0:
            n = n//i
        i += 1
    return i


