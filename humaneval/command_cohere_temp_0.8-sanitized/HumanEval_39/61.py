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
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n % 2 == 0:
        return prime_fib(n // 2)
    else:
        return prime_fib(n - 1) if is_prime(prime_fib(n - 1)) else prime_fib(n // 2)