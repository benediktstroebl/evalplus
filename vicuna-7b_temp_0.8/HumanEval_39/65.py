

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
    if n % 2 == 0:
        return 0
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    # Check if n is a Fibonacci number
    fib = [0, 1, 1]
    for i in range(n-1, -1, -1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]
