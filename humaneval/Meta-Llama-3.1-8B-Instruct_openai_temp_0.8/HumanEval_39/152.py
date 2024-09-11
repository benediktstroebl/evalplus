### Fibonacci and Prime Check
#### A Python Script to Find the N-th Fibonacci Number that is also Prime

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
    Generates the n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number.
    
    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    fib = [0, 1]
    for _ in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
        n (int): The position of the Fibonacci number.
    
    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while True:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the n-th Fibonacci number, and `prime_fib` returns the n-th Fibonacci number that is also prime. The example usage demonstrates how to use the `prime_fib` function to find the first five Fibonacci numbers that are also prime.