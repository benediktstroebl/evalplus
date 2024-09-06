```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    Returns None if the benefits if n is less than 0 or not a prime.
    """
    def is_prime(n: int):
        if n <= 1:
            return False
        if n <= 3:
            return True
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                return False
        return True
    fib = [0]
    fib.append(fib[i+1] for i in range(2, n+1))
    for i in range(n):
        if is_prime(fib[i]):
            return fib[i]
    return None

# Test the function
print(prime_fib(5))
```