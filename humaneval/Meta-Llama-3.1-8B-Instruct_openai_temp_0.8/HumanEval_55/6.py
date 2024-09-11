### Fibonacci Number Generator

The following Python script uses memoization to efficiently calculate the `n`-th Fibonacci number.

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}  # Base cases

    def fib_helper(k: int) -> int:
        """Compute k-th Fibonacci number."""
        if k not in memo:
            # If not in memo, store the result and compute the next numbers
            memo[k] = fib_helper(k - 1) + fib_helper(k - 2)
        return memo[k]

    return fib_helper(n)


if __name__ == "__main__":
    # Test cases
    print(fib(10))  # 55
    print(fib(1))   # 1
    print(fib(8))   # 21
```

### Explanation

The script defines a recursive function `fib_helper` to calculate the `k`-th Fibonacci number. It uses a dictionary `memo` to store the results of previously computed Fibonacci numbers, avoiding redundant computations.

In the `fib` function, it initializes the `memo` dictionary with the base cases (`0` and `1`) and delegates the actual computation to the `fib_helper` function. The `fib_helper` function checks if the `k`-th Fibonacci number is already in the `memo` dictionary; if not, it computes the result recursively and stores it in the dictionary for future use.