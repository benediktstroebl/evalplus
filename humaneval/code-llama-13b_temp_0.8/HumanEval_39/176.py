

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
    if n <= 0:
        raise ValueError("n should be positive integer")
    fibs = [1, 1]
    num, index = 2, 2
    while True:
        fibs.append(num)
        num = fibs[index-1] + fibs[index-2]
        index += 1
        if is_prime(num):
            if len(fibs) >= n:
                return num

