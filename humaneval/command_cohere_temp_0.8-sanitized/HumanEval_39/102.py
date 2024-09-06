from itertools import count, takewhile
def is_prime(n):
    """
    Checks if number is prime
    """
    if n <= 1:
        return False
    for i in count(2):
        if n % i == 0:
            return False
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two Fibonacci numbers
    a, b = 0, 1
    count = 0

    # Loop to find the nth Fibonacci number that is prime
    while count < n:
        # Check if a is prime
        if is_prime(a):
            count += 1
        # Check if b is prime
        if is_prime(b):
            count += 1
        # Use states to calculate the next Fibonacci numbers
        a, b = b, a + b

    # Return the n-th Fibonacci number that is prime
    return a