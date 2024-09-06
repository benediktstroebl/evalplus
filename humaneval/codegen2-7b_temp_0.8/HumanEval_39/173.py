

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
    p = 2
    q = 3
    cnt = 0
    while cnt <= n:
        cnt += 1
        temp = p+q
        p = q
        q = temp
        if p*p+q*q > n:
            break
    return p*q
