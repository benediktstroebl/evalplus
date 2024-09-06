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
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    
    # Calculate the n-th Fibonacci number and verify if it's prime
    n_th_fib = prev_fib + curr_fib
    if is_prime(n_th_fib):
        return n_th_fib
    
    return None