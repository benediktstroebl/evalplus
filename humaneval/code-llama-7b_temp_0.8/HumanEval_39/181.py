

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
        return 0
    p_fib = []
    fib = [0, 1]
    prime_fib = [2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            prime_fib.append(fib[-1])
    return prime_fib[n - 1]

