### Fibonacci Number Generator
#### A Python Function to Calculate the N-th Fibonacci Number

Here's a self-contained Python script that defines a function `fib` to calculate the n-th Fibonacci number.

```markdown
### Code
```python
def memoize(func):
    """Cache the results of expensive function calls."""
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
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

### Explanation

This script defines a function `fib` to calculate the n-th Fibonacci number. It uses memoization to store the results of expensive function calls to optimize performance.

The `memoize` function is used to cache the results of function calls. It checks if the result for a specific input is already cached before computing it.

The `fib` function uses the standard recursive formula for calculating Fibonacci numbers: `fib(n) = fib(n-1) + fib(n-2)`. However, this naive approach is inefficient for large values of `n` because it performs many redundant computations.

By using memoization, we avoid redundant computations and store the results of expensive function calls, which significantly improves performance for large values of `n`.

### Example Usage

In the `if __name__ == "__main__":` block, we demonstrate how to use the `fib` function to calculate the first 10 Fibonacci numbers.

You can run this script to see the Fibonacci numbers printed to the console.