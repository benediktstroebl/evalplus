

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
    assert n > 0, 'n must be positive'
    fib_list = [1, 2]

    if n > 2:
        i = 3
        while True:
            i += 1
            if is_prime(i):
                fib_list.append(i)
            if len(fib_list) == n:
                break
    return fib_list[-1]

