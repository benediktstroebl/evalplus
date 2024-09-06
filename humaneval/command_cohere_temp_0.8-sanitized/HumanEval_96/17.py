from math import sqrt
def is_prime(n):
    """Check if n is a prime number"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def count_up_to(n):
    """Return an array of the first n prime numbers less than n"""
    count = 0
    primes = []
    for num in range(2, n):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes