

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

    n_fib = 2

    while n_fib <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        n_fib += 1

    prime_fib_list = []

    for num in fib_list:
        if is_prime(num):
            prime_fib_list.append(num)

    return prime_fib_list[n - 1]

