### Fibonacci Number Generator
#### Using Memoization for Efficient Computation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Uses memoization to store previously computed Fibonacci numbers,
    reducing the time complexity from exponential to linear.

    Args:
        n (int): The position of the Fibonacci number to generate.

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

    # Initialize a dictionary to store computed Fibonacci numbers
    memo = {0: 0, 1: 1}

    # Define a helper function to perform memoized Fibonacci computation
    def fib_helper(k: int) -> int:
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    # Compute and return the n-th Fibonacci number
    return fib_helper(n)
```

This script uses memoization to efficiently compute Fibonacci numbers. By storing previously computed values in a dictionary, it avoids redundant calculations and reduces the time complexity from exponential to linear.

To use this script, simply call the `fib` function with the desired Fibonacci number position as an argument. For example:

```python
print(fib(10))  # Output: 55
```

You can test the script with different inputs to verify its correctness.