

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
    if n < 0 or n > 200:
        raise ValueError("Invalid value for n")

    fib = [0, 1]
    a, b = fib

    for i in range(n):
        a, b = b, (a + b)
        if b > 1000000:
            if b % 2 == 0:
                break
        fib.append(b)
    return fib[-1]
