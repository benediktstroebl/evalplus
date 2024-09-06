

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

    # find fibonacci sequence
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    # find prime fibonacci numbers
    prime_fib_n = 1
    for i in fib:
        if is_prime(i):
            prime_fib_n += 1
            if prime_fib_n == n:
                return i

    return None
