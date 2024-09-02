

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
        raise ValueError("n must be greater than 0")

    curr_fib = 0
    prev_fib = 1
    fib_num = 1
    prime_fib_num = 0
    count = 0
    while prime_fib_num != n:
        fib_num = curr_fib + prev_fib
        if is_prime(fib_num):
            prime_fib_num += 1
        count += 1
        prev_fib = curr_fib
        curr_fib = fib_num

    return curr_fib

