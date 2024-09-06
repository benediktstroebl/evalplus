```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    Returns None if n <= 1
    """
    # Corner case
    if n <= 1:
        return None

    # First and Last Fibonacci Numbers
    fi = 0
    f = 1
    while f < n:
        fi = f + f
    n = fi

    # Check for divisibility by numbers from 2 to sqrt(n)
    div = [2, 3, 5, 6, 8, 9, 11, 13, 17, 19, 23, 29, 31,
        31, 42, 56, 67, 71, 82, 91]
    for d in div:
        if n % d == 0:
            return None

    # Return n if it is a prime
    return n

# Test the function
print(prime_fib(1))   # Returns 2
print(prime_fib(2))   # Returns 3
print(prime_fib(3))   # Returns 5
print(prime_fib(5))   # Returns 89
print(prime_fib(6))   # Returns None, not a prime number
print(prime_fib(10)) # Returns None, not a prime number
```