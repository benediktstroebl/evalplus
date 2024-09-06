def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_num = fib_1 = 2
        fib_2 = 3
        for _ in range(3, n + 1):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            if is_prime(fib_1):
                fib_num = fib_1
        return fib_num