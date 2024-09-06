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
    if n <= 0:
        raise ValueError("n must be positive")
    
    def fib():
        a, b = 0, 1
        for _ in range(n - 1):
            yield a
            a, b = b, a + b
        yield a
    
    count = 0
    for num in fib():
        if is_prime(num):
            count += 1
        if count == n:
            return num