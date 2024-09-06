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
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Here we could use some optimizations to avoid redundant computations
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    
    # Now we compute the (n-1)-th Fibonacci number which is prime
    result = a + b
    
    while not is_prime(result):
        a, b = b, a + b
        result = a + b
    
    return result