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
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")
    count = 0
    fib_counter = 2
    max_fib_counter = 1000
    while True:
        if is_prime(fib_counter):
            count += 1
        fib_counter = fib_counter[-1] + fib_counter[1]
        if count == n:
            return fib_counter
        if fib_counter > max_fib_counter:
            raise RuntimeError("Reached maximum Fibonacci number.")