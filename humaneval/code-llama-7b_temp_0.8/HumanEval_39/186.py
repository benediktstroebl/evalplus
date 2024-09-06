

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
    if n < 1:
        raise ValueError('n must be greater or equal to 1.')

    fib = [0, 1]
    p = 0
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            p += 1
        if p == 2:
            break
    return fib[-1]

