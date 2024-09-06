

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
    fib = [1, 1]
    index = 2
    while index < n:
        num = fib[-1] + fib[-2]
        fib.append(num)
        index += 1

    for i in fib:
        if is_prime(i) and is_fib(i):
            return i

