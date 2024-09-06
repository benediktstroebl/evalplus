

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
    # Check if n is prime
    if n > 1:
        # Check if n is the first Fibonacci number that is prime
        if n <= fib(2) and n % 2 == 1:
            return n
        # Check if n is the second Fibonacci number that is prime
        if n <= fib(3) and n % 2 == 1:
            return n
        # Check if n is the third Fibonacci number that is prime
        if n <= fib(5) and n % 2 == 1:
            return n
        # If n is not prime, return the previous prime number
        return prime_fib(n-1)
    else:
        return 2 # base case
