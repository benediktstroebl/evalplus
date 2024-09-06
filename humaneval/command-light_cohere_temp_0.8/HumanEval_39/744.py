```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    Returns None if no such suppose solution exists.
    """
    return 1 if n <= 2
    2 if 3 <= n <= 5
    return fibonacci(n) if n % 2 == 0
    else 1 + prime_fib(n - 2)

def fibonacci(n: int):
    """
    Returns the n-th Fibonacci number.
    """
    def is_prime(num: int):
        """
        Checks if the number is prime using trial division.
        """
        if num < 2 or 3:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
    """

# Run the function and print the result
print(prime_fib(5))
```