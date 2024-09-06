

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
    previous_fib, current_fib = 1, 2
    while True:
        if not is_prime(current_fib):
            previous_fib, current_fib = current_fib, previous_fib + current_fib
            continue
        return current_fib

