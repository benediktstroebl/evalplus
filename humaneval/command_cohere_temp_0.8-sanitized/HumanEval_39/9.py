def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    else:
        return next((a if is_prime(a) else b) for a, b in zip(list(range(2, n + 2))[::2], list(range(1, n + 2))[1::2]) if a <= n)