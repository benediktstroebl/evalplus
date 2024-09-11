### prime_fib Function
#### Returns the n-th number in the Fibonacci sequence that is also prime.

```markdown
### Code:
```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
```

### Example Use Cases:
```python
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines a helper function `is_prime` to check if a number is prime, and the main function `prime_fib` to find the n-th Fibonacci number that is also prime. The `prime_fib` function generates Fibonacci numbers and checks each one for primality until it finds the n-th prime Fibonacci number.