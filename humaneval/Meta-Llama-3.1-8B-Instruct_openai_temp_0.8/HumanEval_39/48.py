### Fibonacci Prime Generator
#### Python Script

```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    i = 1
    while True:
        if is_prime(b):
            if i == n:
                return b
        a, b = b, a + b
        i += 1


def prime_fib(n: int):
    """
    Helper function for testing, returns the n-th Fibonacci prime.
    """
    return fibonacci_prime(n)


# Test cases
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5]
    for i in test_cases:
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

### Explanation

This script consists of two main functions:

1.  `is_prime(num: int) -> bool`: Checks if a given number `num` is prime.
2.  `fibonacci_prime(n: int) -> int`: Generates the n-th Fibonacci number that is also prime.

The `fibonacci_prime` function uses the `is_prime` function to filter Fibonacci numbers for primality. It keeps track of the current Fibonacci number `b` and the preceding number `a` in each iteration, updating them according to the Fibonacci sequence. Once it finds a prime Fibonacci number at the correct position `n`, it returns this number.

The `prime_fib` function is a helper function for testing purposes and simply calls `fibonacci_prime` with the given argument `n`.

The script includes test cases for `prime_fib` to demonstrate its correctness. You can run the script to see the output for the specified test cases.