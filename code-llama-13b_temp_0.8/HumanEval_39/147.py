

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
    fib, prime, cur = [0, 1], [2], 1
    while prime[-1] < n:
        cur = fib[-1] + fib[-2]
        fib.append(cur)
        if is_prime(cur):
            prime.append(cur)
    return prime[-1]

