### Prime Fibonacci Sequence Generator
#### Python Script

```markdown
### Code
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
    Returns the nth number in the Fibonacci sequence.
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The nth prime Fibonacci number.
    """
    count = 0
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        num += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

### Explanation
This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime.
2. `fibonacci(n)`: Returns the nth number in the Fibonacci sequence.
3. `prime_fib(n)`: Returns the nth number that is a Fibonacci number and it's also prime.

The `prime_fib(n)` function uses a while loop to generate Fibonacci numbers and checks if each number is prime using the `is_prime(num)` function. When it finds the nth prime Fibonacci number, it returns it.