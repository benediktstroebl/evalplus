### prime_fib Script

```markdown
### prime_fib.py

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
        i += 1


# Example usage:
print(prime_fib(1))  # Should print 2
print(prime_fib(2))  # Should print 3
print(prime_fib(3))  # Should print 5
print(prime_fib(4))  # Should print 13
print(prime_fib(5))  # Should print 89
```

To run the script, save it as `prime_fib.py` and execute it with Python:

```bash
python prime_fib.py
```

You can also use the interactive Python shell to test the functions:

```python
python -i prime_fib.py
```