

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
    number = [2, 3]
    while len(number) < n:
        number.append(number[-1] + number[-2])

    if n > 1:
        return number[n-1]
    else:
        return number[0]
