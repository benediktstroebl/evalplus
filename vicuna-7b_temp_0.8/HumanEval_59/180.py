

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    if n % 2 == 0:
        return n / 2
    if n % 3 == 0:
        return 3 * largest_prime_factor(n // 3)
    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

if __name__ == '__main__':
    for num in range(1, 11):
        print(largest_prime_factor(num))