### Prime Fibonacci Numbers
```python
def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prime_fib(n: int) -> int:
    """
    Return the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```
This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates the nth Fibonacci number, and the `prime_fib` function returns the nth number that is both a Fibonacci number and prime. The script then tests the `prime_fib` function with the first five inputs.