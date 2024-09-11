### Fibonacci Number Generator
#### Using Memoization for Efficient Computation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to generate.

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
    # Create a dictionary to store Fibonacci numbers for memoization
    memo = {0: 0, 1: 1}

    def fib_helper(k: int) -> int:
        # If the Fibonacci number is already in the memo, return it
        if k in memo:
            return memo[k]
        # Otherwise, calculate the Fibonacci number and store it in the memo
        else:
            result = fib_helper(k - 1) + fib_helper(k - 2)
            memo[k] = result
            return result

    return fib_helper(n)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a recursive `fib` function that uses memoization to efficiently compute Fibonacci numbers. The `fib_helper` function is a helper function that performs the actual computation using memoized values.

**How it works:**

1.  The `memo` dictionary stores previously computed Fibonacci numbers for efficient retrieval.
2.  The `fib_helper` function uses the memoized values to calculate the `k`-th Fibonacci number.
3.  If the Fibonacci number is already in the memo, it returns the stored value.
4.  Otherwise, it calculates the Fibonacci number recursively and stores it in the memo.

This approach avoids redundant calculations and significantly improves the performance of the `fib` function for larger inputs.