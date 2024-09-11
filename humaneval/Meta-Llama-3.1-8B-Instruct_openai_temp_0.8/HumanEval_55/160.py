### Fibonacci Number Calculation
#### Using Memoization for Efficient Calculation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number using memoization.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.
    """
    memo = {0: 0, 1: 1}  # Base cases

    def fib_helper(k: int) -> int:
        """Helper function to calculate Fibonacci numbers using memoization."""
        if k not in memo:
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]

    return fib_helper(n)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses memoization to store previously computed Fibonacci numbers, allowing it to calculate the nth Fibonacci number efficiently. The `fib_helper` function uses recursion to calculate Fibonacci numbers, but it stores the results in the `memo` dictionary to avoid redundant computations. The `fib` function serves as the main entry point and initializes the `memo` dictionary with base cases.