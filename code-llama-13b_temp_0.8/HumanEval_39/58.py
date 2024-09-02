

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
    prev_1, prev_2 = 1, 1
    count = 0
    current = prev_1 + prev_2
    while True:
        if is_prime(current) and is_fibonacci(current):
            count += 1
            if count == n:
                return current
        prev_1, prev_2 = prev_2, current
        current = prev_1 + prev_2

