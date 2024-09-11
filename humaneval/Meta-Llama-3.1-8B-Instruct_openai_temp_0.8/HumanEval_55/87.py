### Fibonacci Number Calculation
#### Using Memoization for Efficient Computation

Here's a Python function that calculates the nth Fibonacci number using memoization for efficient computation:

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    memo = {0: 0, 1: 1}  # Initialize memo dictionary with base cases

    def fib_helper(k):
        """Recursive helper function to calculate k-th Fibonacci number."""
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)  # Calculate and store k-th Fibonacci number
        return memo[k]

    return fib_helper(n)

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a top-down approach with memoization to calculate the nth Fibonacci number efficiently. The `memo` dictionary stores previously calculated Fibonacci numbers to avoid redundant computations. The `fib_helper` function recursively calculates the k-th Fibonacci number and stores it in the `memo` dictionary for future use.