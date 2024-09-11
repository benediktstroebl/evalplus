### Fibonacci Number Calculation Script

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Examples:
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
        return fib(n - 1) + fib(n - 2)


# Example usage:
if __name__ == "__main__":
    positions = [1, 8, 10]
    for pos in positions:
        print(f"Fibonacci number at position {pos} is {fib(pos)}")
```

This script defines a recursive function `fib(n)` that calculates the n-th Fibonacci number. The function uses the mathematical property of Fibonacci numbers to reduce the problem size by one in each recursive call.

Please note that this script uses a recursive approach which can be inefficient for large values of `n` due to excessive repeated calculations. For larger inputs, consider using an iterative approach or memoization to improve performance.