def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer")
    
    count = 0
    fib_n = 0
    fib_prev = 1
    while count < n:
        fib_next = fib_prev + fib_n
        if is_prime(fib_next):
            nth_prime_fib = fib_next
            count += 1
        fib_prev = fib_n
        fib_n = fib_next
    return nth_prime_fib