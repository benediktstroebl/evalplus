

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
    if n < 2 or n > 100:
        raise ValueError("Invalid input. n should be greater than 2 and less than 100.")

    f_num = 0
    f_prime = 1

    for i in range(2, n):
        if n % i == 0:
            return None
        elif n % i == 1:
            f_prime = prime_fib(i)
            f_num = f_num * i + f_prime

    return f_num
