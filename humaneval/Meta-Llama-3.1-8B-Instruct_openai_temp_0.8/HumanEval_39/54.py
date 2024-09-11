Here's a Python script that solves the problem:
```markdown
### prime_fib.py

### Function to check if a number is prime
```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
    Args:
    num (int): Number to check
    
    Returns:
    bool: True if the number is prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

### Function to generate Fibonacci sequence
```python
def fibonacci(n: int) -> int:
    """
    fibonacci returns the nth Fibonacci number.
    
    Args:
    n (int): Position of the Fibonacci number to return
    
    Returns:
    int: The nth Fibonacci number
    """
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```

### Function to find the nth number that is a Fibonacci number and a prime number
```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): Position of the Fibonacci number to check for primality
    
    Returns:
    int: The n-th Fibonacci number that is also prime
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        i += 1
```

### Example Usage
```python
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script first checks if a number is prime, then generates Fibonacci numbers, and finally uses these two functions to find the nth number that is a Fibonacci number and a prime number. The `prime_fib` function keeps generating Fibonacci numbers until it finds a prime one, and then it returns this prime Fibonacci number.