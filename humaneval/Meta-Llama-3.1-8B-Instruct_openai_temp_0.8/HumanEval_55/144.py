### Fibonacci Number Generator
#### Problem Description
The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. This script generates the nth Fibonacci number.

#### Solution
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.

    Example:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This script uses an iterative approach to calculate the nth Fibonacci number, which is more efficient than a recursive approach for large values of n. The `fib` function takes an integer `n` as input and returns the nth Fibonacci number. The function uses a simple loop to calculate the Fibonacci numbers up to the nth number. The `if` statement at the beginning of the function handles the base cases where `n` is 0 or 1.