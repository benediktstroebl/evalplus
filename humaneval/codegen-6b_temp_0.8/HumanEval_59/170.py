

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while n % i != 0:
        i += 1
    return i

    # TODO: Write Code Here. What is the name of the largest prime factor?

    # 1st try: The function below is too slow and returns the wrong result. I changed it to the above because it works.
    # But see
    # https://stackoverflow.com/questions/22384031/largest-prime-factor-of-a-number-in-python#22384744
    # This function has the typo in the comments.
    # def large_prime_factor(n: int):
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     if n == 3:
    #         return 3
    #     if n % 2 == 0:
    #         return 2
    #     if n % 3 == 0:
    #         return 3
    #     limit = 1
    #     while n > limit:
    #         limit = limit * 3 + 1
    #         if n % limit == 0:
    #             return limit

    # 2nd try: The function below is much faster than the first one and returns the correct result.
    # def large_prime_factor(n: int):
    #     # Must be a prime.
    #     assert n > 1
    #     if n == 1:
    #         return 1
    #     # Must be even.
    #     assert n % 2 == 0
    #     limit = n ** 0.5
    #     i = 3
    #     while i <= limit:
    #         if n % i == 0:
    #             return i
    #         i += 2
    #     return n

