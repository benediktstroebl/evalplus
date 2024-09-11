```python
import math

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
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b) and count == n:
            return b
        count += 1


# Test cases
if __name__ == "__main__":
    print(prime_fib(1))  # Expected output: 2
    print(prime_fib(2))  # Expected output: 3
    print(prime_fib(3))  # Expected output: 5
    print(prime_fib(4))  # Expected output: 13
    print(prime_fib(5))  # Expected output: 89
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers and checks if they are prime. It uses the `is_prime` function to filter out non-prime Fibonacci numbers. The test cases at the end verify the correctness of the `prime_fib` function.