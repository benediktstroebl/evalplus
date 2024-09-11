### prime_fib.py
```markdown
## prime_fib Function
### Returns the nth number that is a Fibonacci number and a prime number.

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
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number to find.

    Returns:
    int: The nth Fibonacci number that is also a prime number.
    """
    prime_count = 0
    num = 1
    while prime_count < n:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            prime_count += 1
            if prime_count == n:
                return fib_num
        num += 1


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines helper functions `is_prime` to check if a number is prime and `fibonacci` to generate the nth Fibonacci number. Then it uses these helper functions to find the nth Fibonacci number that is also prime in the `prime_fib` function.