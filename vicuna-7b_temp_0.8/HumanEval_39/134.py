

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
    # check if n is prime
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return None
        return n

    # check if n is the n-th Fibonacci number
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return prime_fib(n-1) + prime_fib(n-2)
