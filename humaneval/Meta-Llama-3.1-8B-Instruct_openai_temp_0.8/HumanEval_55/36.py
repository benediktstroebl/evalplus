```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a recursive function `fib(n)` to calculate the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

However, this recursive solution has a high time complexity for large inputs due to the repeated calculation of the same Fibonacci numbers. For a more efficient solution, consider using an iterative approach or memoization with dynamic programming.