def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.

    Args:
        n (int): The index of the desired number.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find the next suitable Fibonacci number that is prime
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        next_prime_fib = a + b

        return next_prime_fib