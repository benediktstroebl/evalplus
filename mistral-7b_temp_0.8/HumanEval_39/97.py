

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
    # n is 0, 1, or larger
    if n == 0 or n == 1:
        return n
    else:
        # n > 1
        n_minus_one = 1
        n_minus_two = 0
        while True:
            # n_minus_one < n
            if n_minus_one < n:
                # n_minus_one == n:
                if n_minus_one == n:
                    return n_minus_one
                # n_minus_one < n
                n_minus_one += n_minus_two
                n_minus_two = n_minus_one - n_minus_two
            # n_minus_one > n:
            else:
                # n_minus_one is prime:
                if is_prime(n_minus_one):
                    return n_minus_one
                # n_minus_one is composite:
                else:
                    # n_minus_one == n:
                    if n_minus_one == n:
