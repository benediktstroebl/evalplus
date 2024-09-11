### Fibonacci Number Function in Python
#### Using Memoization for Efficient Computation
```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    This function uses memoization to store previously computed Fibonacci numbers
    for efficient computation of larger values.

    Args:
        n (int): The position of the Fibonacci number to return.

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
    memo = {0: 0, 1: 1}  # Store base cases

    def fib_recursive(k):
        """Helper function to compute k-th Fibonacci number recursively."""
        if k not in memo:  # If not in memo, compute and store
            memo[k] = fib_recursive(k-1) + fib_recursive(k-2)
        return memo[k]

    return fib_recursive(n)


# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```
This script defines a recursive function `fib` that uses memoization to store previously computed Fibonacci numbers. The `fib_recursive` helper function is used to compute the k-th Fibonacci number recursively, and the results are stored in the `memo` dictionary for efficient retrieval.