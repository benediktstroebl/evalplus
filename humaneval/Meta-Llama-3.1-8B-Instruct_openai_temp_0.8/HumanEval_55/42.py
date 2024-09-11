### Fibonacci Number Calculation
#### Using Top-Down Dynamic Programming Approach

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

    Fibonacci numbers are a series of numbers where a number is the addition of the last two numbers, 
    starting with 0 and 1.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The n-th Fibonacci number.

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

    # Create a dictionary to store the Fibonacci numbers for memoization
    memo = {0: 0, 1: 1}

    def fib_helper(k: int) -> int:
        """Recursive helper function to calculate the k-th Fibonacci number."""
        if k in memo:
            return memo[k]
        result = fib_helper(k - 1) + fib_helper(k - 2)
        memo[k] = result
        return result

    return fib_helper(n)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a top-down dynamic programming approach to calculate the n-th Fibonacci number. It employs memoization to store previously calculated Fibonacci numbers, which significantly improves performance for large values of n.