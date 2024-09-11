### Prime Fibonacci Numbers
#### Python Script

```python
import math

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num: The number to check.
    
    Returns:
    True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Returns the n-th number in the Fibonacci sequence.
    
    Args:
    n: The position of the number in the Fibonacci sequence.
    
    Returns:
    The n-th Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is both a Fibonacci number and prime.
    
    Args:
    n: The position of the number in the sequence.
    
    Returns:
    The n-th prime Fibonacci number.
    """
    i = 1
    count = 0
    while True:
        num = fibonacci(i)
        if is_prime(num):
            count += 1
            if count == n:
                return num
        i += 1


# Test the function
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script first defines helper functions `is_prime` to check if a number is prime and `fibonacci` to generate the n-th Fibonacci number. The `prime_fib` function uses these helpers to find the n-th prime Fibonacci number. The script then tests the `prime_fib` function with the provided examples.