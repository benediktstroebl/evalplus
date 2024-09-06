import math
def is_prime(n):
    """Check if an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    count = 0
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
            count += 1
        if count == n:
            break
    return primes