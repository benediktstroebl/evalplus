### Fibonacci Number Generator
#### A Self-Contained Python Script

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to generate.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script uses a recursive approach to calculate the n-th Fibonacci number. However, please note that this method is not efficient for large values of n due to its exponential time complexity. For a more efficient solution, consider using dynamic programming or memoization techniques.

**Note:** The script is wrapped in a `if __name__ == "__main__":` block to ensure that the example usage is only executed when the script is run directly, not when it's imported as a module.