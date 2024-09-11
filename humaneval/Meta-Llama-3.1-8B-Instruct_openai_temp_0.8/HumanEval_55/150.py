### Fibonacci Number Calculation
#### Using Memoization for Efficient Computation

```markdown
## Overview
This script provides a function to calculate the nth Fibonacci number using memoization.

## Code

```python
def memoize(f):
    """Cache the results of expensive function calls."""
    cache = dict()

    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result

    return memoized_function


@memoize
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

## Explanation
- The `memoize` function is a decorator that caches the results of expensive function calls.
- The `fib` function uses memoization to efficiently calculate the nth Fibonacci number.
- The `if __name__ == "__main__"` block contains example usage of the `fib` function.
```