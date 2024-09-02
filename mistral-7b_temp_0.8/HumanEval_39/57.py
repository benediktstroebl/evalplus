

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
        return "n must be positive"

    # Fibonacci sequence
    a, b = 0, 1
    fib = []
    while len(fib) < n:
        fib.append(a)
        a, b = b, a + b
    fib.append(a)

    # Filtering primes
    result = []
    for i in fib:
        if i > 1 and all(i % k for k in range(2, i) if i % k == 0):
            result.append(i)
    return result[n-1]

