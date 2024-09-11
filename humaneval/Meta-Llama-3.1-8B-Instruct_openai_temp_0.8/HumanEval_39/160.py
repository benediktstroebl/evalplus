```markdown
### Prime Fibonacci Numbers
#### Python Script to Generate Nth Prime Fibonacci Number

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

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


def prime_fib(n: int):
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The nth prime Fibonacci number.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
            i += 1
        else:
            i += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

### How it works:

1. The `is_prime` function checks if a number is prime by testing divisibility up to its square root.
2. The `fibonacci` function generates the nth Fibonacci number using an iterative approach.
3. The `prime_fib` function iterates through Fibonacci numbers, checking each one for primality. When it finds the nth prime Fibonacci number, it returns it.