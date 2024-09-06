def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        for _ in range(3, n + 1):
            c = a + b
            a, b = b, c
        return b