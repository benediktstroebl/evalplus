def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th Fibonacci number that is also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(3, n + 1):
        next_fib = prev_fib + curr_fib
        if is_prime(next_fib):
            return next_fib
        prev_fib, curr_fib = curr_fib, next_fib
    
    # Shouldn't reach this line if the function is correct
    return None