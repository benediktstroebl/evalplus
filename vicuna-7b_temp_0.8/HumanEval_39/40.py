

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
    # Fibonacci sequence
    a, b = 0, 1
    result = 1
    for _ in range(n-1):
        result, a, b = b, a + result
    # check if the number is prime
    for i in range(n-1):
        if result % i != 0:
            return result
    return result
