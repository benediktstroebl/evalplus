### Fibonacci Number Calculation
#### Using Memoization for Efficient Computation

Below is a Python function that calculates the n-th Fibonacci number using memoization. This approach avoids redundant calculations by storing previously computed Fibonacci numbers in a dictionary.

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to calculate.

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
    memo = {0: 0, 1: 1}  # Initialize dictionary with base cases

    def fib_helper(k):
        """Helper function to calculate k-th Fibonacci number."""
        if k not in memo:
            # If k is not in memo, calculate it using k-1 and k-2
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]

    return fib_helper(n)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that uses a helper function `fib_helper(k)` to calculate the k-th Fibonacci number. The helper function uses memoization to store previously computed Fibonacci numbers in a dictionary `memo`. This approach efficiently calculates the n-th Fibonacci number by avoiding redundant calculations.