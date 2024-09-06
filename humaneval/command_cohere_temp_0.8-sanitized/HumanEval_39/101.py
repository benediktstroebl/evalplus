def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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
        fib_n = 5
        prev_fib = 2
        while True:
            # Check if fib_n is prime
            if is_prime(fib_n):
                return fib_n
            # Update fib_n for next iteration
            fib_n, prev_fib = prev_fib, fib_n + prev_fib
            if fib_n == n:
                break