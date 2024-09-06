

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO
    num = n
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1

    while num != 1:
        count = 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 1
                num = num // i
                break

        if num != 1:
            count = 0
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 1
                    num = num // i
                    break

    return num

