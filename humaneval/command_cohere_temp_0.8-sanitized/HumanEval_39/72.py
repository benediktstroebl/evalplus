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
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two variables for the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n - 1):
        # Each iteration yields the next Fibonacci number
        a, b = b, a + b
    # Return the n-th Fibonacci number if it is also a prime
    if is_prime(a):
        return a