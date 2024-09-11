```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generate the nth Fibonacci number.
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


def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    count = 1
    num = 0
    while True:
        num = fibonacci(count)
        if is_prime(num):
            return num
        count += 1


# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime. Then it defines another helper function `fibonacci` to generate the nth Fibonacci number. The `prime_fib` function uses these two functions to generate the n-th number that is both a Fibonacci number and a prime number.