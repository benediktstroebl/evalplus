

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
    primes = [2]
    ans = 1
    cur = 2
    while ans <= n:
        cur = cur + primes[-1]
        if is_prime(cur):
            primes.append(cur)
        ans = ans + len(primes)
    return cur
