### Prime Fibonacci Numbers
#### Python Script

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


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    i = 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            if i == n:
                return b
            i += 1


# Test the function
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines two functions: `is_prime` to check if a number is prime and `prime_fib` to find the n-th prime Fibonacci number. The `prime_fib` function uses a loop to generate Fibonacci numbers and checks each one with `is_prime` to see if it's also prime. When it finds the n-th prime Fibonacci number, it returns it. The script then tests the `prime_fib` function with the first 5 inputs.