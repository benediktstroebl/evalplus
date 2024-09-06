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
    
    # Here we manually generate the first few Fibonacci numbers
    # The recursive relation only really works for larger values
    fib = [0, 1]
    for _ in range(10):  # We can stop early if we find a prime
        next_fib = fib[-1] + fib[-2]
        if is_prime(next_fib):
            return next_fib
        fib.append(next_fib)
    
    # After trying 10 manually generated Fibonacci numbers,
    # we can return the next one using the recursive relation
    return prime_fib(n - 1) if is_prime(prime_fib(n - 1)) else None