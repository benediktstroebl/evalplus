

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
    fib = [0, 1]
    index = 2
    while index <= n:
        fib.append(fib[-1] + fib[-2])
        index += 1

    index = 2
    while index <= n:
        if is_prime(fib[index]) and is_prime_fibonacci(fib[index]):
            return fib[index]
        index += 1

    return -1

