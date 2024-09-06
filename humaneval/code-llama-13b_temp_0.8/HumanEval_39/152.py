

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
        raise ValueError("n must be >= 1.")
    fib_list = [0, 1]
    prime_list = []
    prime_index = 1
    while len(prime_list) < n:
        fib_list.append(fib_list[-2] + fib_list[-1])
        if is_prime(fib_list[-1]):
            prime_list.append(fib_list[-1])
            prime_index += 1
    return prime_list[n - 1]

