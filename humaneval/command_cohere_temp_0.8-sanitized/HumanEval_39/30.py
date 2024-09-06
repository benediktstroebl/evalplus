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
    Generates the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the Fibonacci number to generate.

    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    def fibonacci_sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

    if n == 0 or n == 1:
        return 2  # The first two prime Fibonacci numbers are 2 and 3
    else:
        return next(i for i in fibonacci_sequence(n) if is_prime(i))