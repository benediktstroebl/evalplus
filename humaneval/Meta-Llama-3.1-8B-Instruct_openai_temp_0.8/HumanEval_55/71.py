### Fibonacci Number Calculation
#### A Self-Contained Python Script

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

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


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python script defines a recursive function `fib` that calculates the n-th Fibonacci number. The function uses the mathematical property of Fibonacci sequence where each number is the sum of the two preceding ones. The base case for the recursion is when `n` is less than or equal to 1, in which case the function returns `n` directly.

Please note that while the recursive approach is straightforward and easy to implement, it has a high time complexity of O(2^n) due to the repeated calculations involved. For larger values of `n`, a more efficient approach would be to use dynamic programming or memoization to store and reuse previously calculated Fibonacci numbers.