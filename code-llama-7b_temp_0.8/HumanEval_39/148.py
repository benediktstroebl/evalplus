

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
    # Base cases
    if n == 1:
        return 2
    if n == 2:
        return 3
    # Finding n-th Fibonacci number
    Fn = fib(n + 1)
    # Checking if the number is prime
    while not is_prime(Fn):
        Fn = Fn - 1
    return Fn

