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
    Generates the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_prime_fib = 3
    current_prime_fib = 5
    count = 0

    while count < n - 2:
        if is_prime(current_prime_fib):
            prev_prime_fib = current_prime_fib
            current_prime_fib = (prev_prime_fib + current_prime_fib) % infinity
            count += 1
        else:
            current_prime_fib = (prev_prime_fib + current_prime_fib) % infinity

    return current_prime_fib