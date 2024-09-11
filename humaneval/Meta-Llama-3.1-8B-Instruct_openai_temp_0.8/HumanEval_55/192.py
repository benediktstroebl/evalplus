### Fibonacci Number Calculator
#### Using Memoization

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.

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
    memo = {0: 0, 1: 1}  # Base cases: F(0) = 0, F(1) = 1

    def fib_helper(k: int) -> int:
        """Recursive helper function to calculate k-th Fibonacci number."""
        if k not in memo:
            # If k is not in memo, calculate it and store in memo
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    return fib_helper(n)

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a technique called memoization to store and reuse previously calculated Fibonacci numbers. This significantly reduces the time complexity of the function from exponential to linear.