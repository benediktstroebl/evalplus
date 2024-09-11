```markdown
## Prime Fibonacci Numbers

This script defines a function `prime_fib(n)` that returns the `n-th` number that is both a Fibonacci number and a prime number.

### Code

```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.

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


def is_fibonacci(num: int) -> bool:
    """
    Helper function to check if a number is a Fibonacci number.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    x = 0
    y = 1
    while y < num:
        z = x + y
        x = y
        y = z
    return y == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while True:
        if is_fibonacci(num) and is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

### Explanation

This script uses three helper functions:

*   `is_prime(num)`: Checks if a number is prime by checking divisibility up to the square root of the number.
*   `is_fibonacci(num)`: Checks if a number is a Fibonacci number by generating Fibonacci numbers iteratively and checking if the current number matches the target.
*   `prime_fib(n)`: Finds the `n-th` Fibonacci number that is also prime by iterating through Fibonacci numbers and checking if each one is prime.

The `prime_fib(n)` function uses a counter to keep track of the position of the Fibonacci numbers that are also prime and returns the `n-th` such number.