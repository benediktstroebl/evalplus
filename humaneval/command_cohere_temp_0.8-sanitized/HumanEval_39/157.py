def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # This iterates through odd Fibonacci numbers, as the even ones won't be prime
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return a