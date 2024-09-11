## Fibonacci Number Generator
### A Python Script to Calculate the N-th Fibonacci Number

Here is a Python script that uses a recursive approach to calculate the n-th Fibonacci number.

```python
def memoize(func):
    """Decorator to memoize the function results for faster execution."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fib(n: int):
    """Return n-th Fibonacci number.
    
    This function uses memoization to store previously calculated Fibonacci numbers,
    which significantly improves performance for large inputs.
    
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script defines a `fib` function that uses memoization to store previously calculated Fibonacci numbers. This significantly improves performance for large inputs, as it avoids redundant calculations. The script also includes example usage and docstrings for clarity.