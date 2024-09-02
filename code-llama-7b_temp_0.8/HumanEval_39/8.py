

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
    prime_fib_set = set()
    i = 2
    prime_fib_set.add(i)
    while len(prime_fib_set) != n:
        i += 1
        if is_prime(i):
            i_is_fib = is_fib(i)
            if i_is_fib:
                prime_fib_set.add(i)
    return i

