### Fibonacci Number Generator

Here's a Python function that generates the n-th Fibonacci number using recursion and memoization:

```python
def fib(n: int):
    """Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21

    Raises:
        ValueError: If n is a negative integer.
    """
    memo = {0: 0, 1: 1}  # Initialize the memo dictionary

    def fib_helper(k: int) -> int:
        """Helper function to calculate the k-th Fibonacci number."""
        if k not in memo:
            # If the Fibonacci number is not cached, calculate it
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]

    if n < 0:
        # Raise an error if n is a negative integer
        raise ValueError("n must be a non-negative integer.")
    return fib_helper(n)
```

### Explanation

This script uses a recursive approach with memoization to improve performance. The `fib` function takes an integer `n` as input and returns the `n-th` Fibonacci number.

The `fib_helper` function is a recursive helper function that calculates the `k-th` Fibonacci number. If the Fibonacci number is not cached in the `memo` dictionary, it calculates the result by recursively calling itself with `k-1` and `k-2`.

The `fib` function initializes the memo dictionary with the base cases `F(0) = 0` and `F(1) = 1`. It then calls the `fib_helper` function with the input `n` and returns the result.

Note that this implementation raises a `ValueError` if `n` is a negative integer, as the Fibonacci sequence is only defined for non-negative integers.