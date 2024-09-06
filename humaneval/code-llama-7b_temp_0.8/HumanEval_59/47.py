

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # The number must be greater than 1
    while n > 1:
        # This is a prime
        if n % 2 == 1:
            # print(n)
            for i in range(3, n, 2):
                # print(i)
                # print(n % i)
                if n % i == 0:
                    n = n / i
                    break
            else:
                return n
        # This is not a prime
        else:
            # print(n)
            for i in range(3, n, 2):
                # print(i)
                # print(n % i)
                if n % i == 0:
                    n = n / i
                    break
            else:
                return n

