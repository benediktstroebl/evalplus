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
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    
    # Calculate the next potential fibonacci number
    next_fib = prev_fib + curr_fib
    
    while not is_prime(next_fib):
        next_fib += curr_fib

    return next_fib