

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

    fib_num = 1
    previous_fib = 1
    previous_prime = 2
    while fib_num <= n:
        fib_num = previous_fib + previous_prime
        previous_fib = fib_num - previous_prime
        if is_prime(fib_num):
            previous_prime = fib_num
        else:
            continue
    return fib_num
    
    
