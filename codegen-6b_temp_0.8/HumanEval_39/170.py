

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
    result = [2, 3]
    i = 0
    while len(result) < n:
        i += 1
        fib = result[-1] + result[-2]
        if is_prime(fib):
            result.append(fib)
    return result[n - 1]

