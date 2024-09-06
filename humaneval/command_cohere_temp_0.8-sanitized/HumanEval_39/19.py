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
        raise ValueError("n must be positive")
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Iterate through Fibonacci numbers until we find the n-th prime one
        count_primes = 0
        fib_number = fibonacci(n)
        while not is_prime(fib_number):
            fib_number = fibonacci(n)
            count_primes += 1
        return fib_number