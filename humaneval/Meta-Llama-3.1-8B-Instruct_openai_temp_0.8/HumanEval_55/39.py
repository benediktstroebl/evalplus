### Fibonacci Number Calculation
#### Using Dynamic Programming

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to be calculated.

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

    fib_table = [0, 1]
    for i in range(2, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

In this script, we use dynamic programming to store the Fibonacci numbers in a table (`fib_table`). This approach reduces the time complexity to O(n) compared to the naive recursive approach, which has a time complexity of O(2^n).