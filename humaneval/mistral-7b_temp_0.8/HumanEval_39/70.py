

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

    fib_list = [1, 1]
    nth_fib = 0
    nth_prime = 0
    for i in range(2, n + 1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        if is_prime(fib_list[-1]):
            nth_prime = fib_list[-1]
        if is_prime(fib_list[-1]) and is_prime(fib_list[-2]):
            nth_fib = fib_list[-1]
    return nth_fib, nth_prime

