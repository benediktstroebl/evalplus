

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
    current = 0
    fib_i = 1
    fib_prev = 1
    prime_nums = [2]

    while current <= n:
        fib_i = fib_prev + fib_i
        fib_prev = fib_i - fib_prev
        if is_prime(fib_i):
            prime_nums.append(fib_i)
            current += 1
    return prime_nums[n]

