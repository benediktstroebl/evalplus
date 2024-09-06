

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Check if n is a prime number
    if n % 2 != 0:
        return 2
    if n % 3 == 0:
        return 3
    # Calculate the first two numbers of the Fibonacci sequence
    a, b = 0, 1
    # Loop until we find a prime number
    while True:
        # Calculate the next number in the Fibonacci sequence
        c = a + b
        # Check if the next number is prime
        if is_prime(c):
            return c
        # Increment a and b if the next number is not prime
        if not is_prime(c):
            a, b = b, a + b
        # Check if the current number is the n-th number
        if c == n:
            return n