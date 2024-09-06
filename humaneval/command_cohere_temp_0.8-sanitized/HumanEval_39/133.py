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
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # This section calculates nth Fibonacci number and then filters out non-prime numbers.
        x, y = 0, 1
        for _ in range(n - 3):
            x, y = y, x + y
        num = x if is_prime(x) else y if is_prime(y) else x + y
        return num