

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

    fib = [0, 1]
    i = 1
    while len(fib) < n:
        if is_prime(fib[-1]):
            fib.append(fib[-1] + fib[-2])
        else:
            fib.append(fib[-1] + fib[-2] + 1)
        i += 1
    return fib[-1]
