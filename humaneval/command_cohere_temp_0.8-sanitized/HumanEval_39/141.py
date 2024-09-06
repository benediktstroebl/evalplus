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
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is also prime. Requires positive int input.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input n should be a positive integer.")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if is_prime(a) else b if is_prime(b) else None