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
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    # Calculate the n-th Fibonacci number and check if it's prime
    result = prev + curr
    while not is_prime(result):
        result -= prev
        if result < 0:
            return None
    
    return result