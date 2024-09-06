

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
    if n <= 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    # Start with the first prime number.
    p = 2
    f = 1
    f_n_minus_2 = 1
    f_n_minus_1 = 1
    for _ in range(2, n):
        # Compute the next Fibonacci number.
        f = f_n_minus_1 + f_n_minus_2
        # If it's even, divide by 2.
        while f % 2 == 0:
            f //= 2
        # If it's not even, but it's odd, then multiply by p and divide by 2.
        if f % 2 == 1:
            f = (f * p + 1) // 2
        # If it's not even, but it's divisible by p, then divide by p.
        while f % p == 0:
            f //= p
        # If f_n-1 is not equal to f, then make it equal to f and
        # update f_n-2 to be equal to f_n-1.
        if f_n_minus_1 != f:
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = f
            p += 1

    return f

