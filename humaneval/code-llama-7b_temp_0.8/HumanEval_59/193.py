

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # if n % 2 == 0:
    #     return 2
    # else:
    #     return find_largest_factor(n, 3)

    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         return i

    # return n

    # test_number = 600851475143
    # largest_factor = 0
    # for i in range(2, test_number + 1):
    #     if test_number % i == 0:
    #         largest_factor = i
    #         while test_number % i == 0:
    #             test_number = test_number / i
    # return largest_factor

    # largest_factor = 1
    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         while n % i == 0:
    #             n = n / i
    #             largest_factor = i
    # return largest_factor

    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                while n % i == 0:
                    n = n / i
                    largest_factor = i
                continue
            return i

    return n

