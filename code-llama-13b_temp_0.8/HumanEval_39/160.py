

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
    cur_prime = 2
    cur_fib = 1
    cur_fib_back1 = 0
    cur_fib_back2 = 0
    cur_fib_back3 = 0
    while n > 0:
        if cur_fib > cur_prime and is_prime(cur_fib):
            cur_prime = cur_fib
            n -= 1
        cur_fib_back3 = cur_fib_back2
        cur_fib_back2 = cur_fib_back1
        cur_fib_back1 = cur_fib
        cur_fib = cur_fib_back1 + cur_fib_back2
    return cur_prime

