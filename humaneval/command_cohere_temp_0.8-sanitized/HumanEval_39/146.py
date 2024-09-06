def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is positive
    n = abs(n)
    if n == 1:
        return 2
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if is_prime(a) else b if is_prime(b) else -1