

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

    if n == 1:
        return 2
    prev, curr = 1, 2
    i = 2
    while i < n:
        prev, curr = curr, curr + prev
        i += 1
        if is_prime(curr):
            continue
        else:
            curr += 1
            i -= 1
    return curr
