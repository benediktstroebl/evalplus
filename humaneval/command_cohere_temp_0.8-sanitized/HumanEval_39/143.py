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
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # First Fibonacci number that is prime
    fib_start = 5
    # Second Fibonacci number that is prime
    fib_end = 89
    
    # Iterate through the Fibonacci numbers in reverse
    for i in range(n - 1, 0, -1):
        if is_prime(fib_end):
            return fib_end
        a, b = fib_end, fib_start
        fib_start = a + b
        fib_end = a * 2 + b