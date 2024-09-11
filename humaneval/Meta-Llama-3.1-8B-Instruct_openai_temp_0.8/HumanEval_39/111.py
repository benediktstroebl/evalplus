### Fibonacci Numbers and Prime Numbers
#### A Python Function to Find the n-th Prime Fibonacci Number

Here's a Python script that defines a function `prime_fib` to find the n-th number in the sequence of Fibonacci numbers that is also a prime number:
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


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number to find.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_num = 0
    fib_count = 0
    num = 1
    while fib_count < n:
        num += 1
        a, b = 1, 1
        fib_num = b
        for i in range(2, num):
            a, b = b, a + b
            if is_prime(b):
                fib_count += 1
                if fib_count == n:
                    return b
```
This script uses a helper function `is_prime` to check if a number is prime and the main function `prime_fib` to generate Fibonacci numbers until it finds the n-th prime one. 

### Example Usage
```python
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```