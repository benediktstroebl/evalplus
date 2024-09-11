### Fibonacci Number Generator
#### Using Memoization for Efficient Calculation
```markdown
```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number using memoization.

    This function stores the results of expensive function calls
    and returns the cached result when the same inputs occur again.

    Args:
        n (int): The position of the Fibonacci number to be generated.

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
    memo = {0: 0, 1: 1}  # Initialize memoization dictionary

    def fib_helper(k: int) -> int:
        """A helper function that uses memoization to calculate Fibonacci numbers."""
        if k not in memo:
            # If the result is not in the memo dictionary, calculate it and store it
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]

    return fib_helper(n)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number using memoization. The `fib_helper` function is a recursive helper function that stores the results of previously calculated Fibonacci numbers in the `memo` dictionary. This approach significantly improves the performance of the function for large values of `n`.

When you run this script, it will print the first 10 Fibonacci numbers, along with examples for the 1st and 8th Fibonacci numbers, as specified in the docstring.