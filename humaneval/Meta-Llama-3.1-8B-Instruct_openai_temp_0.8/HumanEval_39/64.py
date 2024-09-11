### Fibonacci Prime Generator

Below is a Python script that generates the n-th Fibonacci prime number.

```markdown
### Fibonacci Prime Generator

This script generates the n-th Fibonacci prime number using the property of Fibonacci numbers and prime number checks.

### Code

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): Number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_prime(n: int) -> int:
    """
    Generates the n-th Fibonacci prime number.

    Args:
    n (int): Index of the Fibonacci prime number to generate.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {fibonacci_prime(i)}")
```

### Explanation

1.  The `is_prime` function checks if a number is prime by trying to divide it by numbers up to its square root.
2.  The `fibonacci_prime` function generates Fibonacci numbers and checks if each is prime using the `is_prime` function.
3.  It keeps track of the count of prime Fibonacci numbers and returns the n-th prime Fibonacci number.

You can run this script to generate the first n Fibonacci prime numbers.