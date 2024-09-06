def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # This section calculates the n-th Fibonacci number while ensuring it is prime
    fib_n = 0
    fib_prev = 0
    fib_next = 1
    while fib_next < n:
        fib_prev, fib_n, fib_next = fib_n, fib_next, fib_next + fib_prev
        if is_prime(fib_n):
            return fib_n
        fib_n += 1
    
    # If we reach this point, n is too large and beyond the Fibonacci sequence
    return fib_n