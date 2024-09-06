def is_prime(n):
    """
    Checks if a number is prime
    """
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
def prime_fib(n):
    """
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib, prev = 0, 1
    for _ in range(n - 2):
        fib, prev = prev, fib + prev
    # Search for primes between fib(n-2) and fib(n-1)
    for num in range(max(fib - 2, 2), fib):
        if is_prime(num):
            return num
    raise ValueError(f"No prime Fibonacci number for n = {n}")