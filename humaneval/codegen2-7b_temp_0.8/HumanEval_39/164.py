

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
    i = 1
    j = 2
    n_max = 10001
    
    while True:
        if n <= n_max:
            if is_prime(n):
                return n
            else:
                return i
        else:
            i += j
            j += i

        n += 1

