```python
def memoize(func):
    """Cache the results of expensive function calls and return the cached result when the same inputs occur again."""
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
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

This script uses memoization to store the Fibonacci numbers as they are calculated. This is a technique that can greatly speed up the calculation of Fibonacci numbers for large n, as it avoids redundant calculations.

When you run this script, it will print out the first 10 Fibonacci numbers.