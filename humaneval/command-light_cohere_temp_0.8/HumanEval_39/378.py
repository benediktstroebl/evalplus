```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is also prime.
    Returns None if n < 1.
    """
    prime_fibonacci(1)
    if n <= 1:
        return None
    else:
        # Check if the n-th Fibonacci number is divisible by any prime numbers except 2
        for num in range(3, n + 1):
            if fibonacci(num) % 2 == 0:
                return None
        else:
            # Calculate the n-th Fibonacci number and check if it's prime
            fibonacci(n) = fibonacci(n) + fibonacci(n - 1)
            if is_prime(fibonacci(n)):
                return fibonacci(n)
            else:
                continue

def fibonacci(n: int):
    """
    Returns the n-th Fibonacci number.
    """
    # n-th Fibonacci number
    if n <= 0:
        return None
    else:
        return n

def is_prime(n: int):
    """
    Checks if n is a prime number.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
prime_fibonacci(10)
``` 
This code defines a Python function called `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime. It does this by iterating through the primes (other than 2) until the square of the current number exceeds the input value.