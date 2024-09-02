

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
    # two first prime Fibonacci numbers
    prev_prev = 2
    prev = 3
    result = 0
    fib_number = 1
    while fib_number <= n:
        result = prev + prev_prev
        if is_prime(result):
            fib_number += 1
        prev_prev = prev
        prev = result
    return result

