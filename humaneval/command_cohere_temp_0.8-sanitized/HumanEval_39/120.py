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
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_prev = 2
    prev = 3
    fibonacci_number = 0
    count = 0
    
    while count < n - 1:
        fibonacci_number = prev + prev_prev
        prev_prev = prev
        prev = fibonacci_number
        count += 1
        
    # Calculate the n-th Fibonacci number without overflow
    fibonacci_number += (prev * (n - 2)) // 2
    
    return fibonacci_number if is_prime(fibonacci_number) else None