def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, n):
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
    
    prev_prev = 2
    prev = 3
    count = 3
    
    while count < n:
        if is_prime(prev):
            nth = prev
            break
        prev_prev, prev = prev, prev_prev + prev
        count += 1
    
    return nth