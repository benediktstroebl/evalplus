from math import sqrt
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
def is_prime(n: int) -> bool:
    """Check if the number is prime"""
    if n < 2:
        return False
    for p in PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False
    return True
def count_up_to(n: int) -> list:
    """Yields the first n prime numbers less than n"""
    count: list = []
    for number in range(2, n):
        if is_prime(number):
            count.append(number)
            if len(count) == n:
                break
    return count