Here's a Python script that calculates the n-th Fibonacci number using memoization to improve performance:

```markdown
# Fibonacci Number Calculator
=====================================

This script calculates the n-th Fibonacci number using memoization.

### Code

```python
def memoize(func):
    """Decorator to memoize a function."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    @memoize
    def fib_helper(k: int):
        """Helper function to calculate k-th Fibonacci number."""
        if k <= 1:
            return k
        return fib_helper(k - 1) + fib_helper(k - 2)

    return fib_helper(n)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

### Explanation

This script uses a helper function `fib_helper` with memoization to calculate the k-th Fibonacci number. The `fib` function calls `fib_helper` with the given `n` as an argument.

The `memoize` decorator is used to cache the results of `fib_helper` for faster lookups.

Note that this script has a time complexity of O(n) due to memoization, making it more efficient than the naive recursive approach with a time complexity of O(2^n).