```python
def memoize(func):
    """A decorator that caches the results of expensive function calls."""
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
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses a technique called memoization to improve the performance of the recursive `fib` function. Memoization stores the results of expensive function calls so they can be reused instead of recalculated. 

In this case, the `fib` function is only calculated once for each input, significantly improving performance for large inputs. The `memoize` decorator is a reusable function that can be applied to other functions that benefit from memoization.