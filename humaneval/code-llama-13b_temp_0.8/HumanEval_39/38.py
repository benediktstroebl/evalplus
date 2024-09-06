

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
    nth_fib = [1, 1]
    while True:
        nth_fib.append(nth_fib[-1] + nth_fib[-2])
        if is_prime(nth_fib[-1]) and is_prime(nth_fib[-2]):
            return nth_fib[n]

