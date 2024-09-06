

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

    result = 0
    count = 0
    # We need to stop when 2*n'th fib number is bigger than n.
    # 2*(10**9) == 200000000
    while result < n:
        count += 1
        result = fib(count)
        if is_prime(result):
            return result

