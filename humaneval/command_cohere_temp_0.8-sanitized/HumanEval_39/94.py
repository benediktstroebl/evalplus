from collections import deque
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
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib = deque([0, 1])
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
        
    while len(fib) > 0 and not is_prime(fib[0]):
        fib.popleft()
        
    if len(fib) == 0:
        return None
    else:
        return fib[0]