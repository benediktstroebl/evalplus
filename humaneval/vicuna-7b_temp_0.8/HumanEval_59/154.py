

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if not n % 2:
        return n + 1
    if n % 3 == 0:
        return 3 * largest_prime_factor(n // 3)
    if n % 5 == 0:
        return 5 * largest_prime_factor(n // 5)
    if n % 7 == 0:
        return 7 * largest_prime_factor(n // 7)
    if n % 2 == 0:
        return 2 * largest_prime_factor(n - 1)
    for x in range(2, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return 2 * largest_prime_factor(n // x)
    return 2 * n // 3

if __name__ == '__main__':
    n = int(input().strip())
    print(largest_prime_factor(n))