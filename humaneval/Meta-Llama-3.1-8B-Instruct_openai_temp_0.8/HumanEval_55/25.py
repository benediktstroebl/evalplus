### Fibonacci Number Calculator
#### Recursive and Iterative Implementations

```python
def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number using recursion.
    
    Args:
    n (int): Position of the Fibonacci number.

    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def memoize(func):
    cache = dict()
    
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized_func


@memoize
def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number using iteration and memoization.
    
    Args:
    n (int): Position of the Fibonacci number.

    >>> fib_iterative(10)
    55
    >>> fib_iterative(1)
    1
    >>> fib_iterative(8)
    21
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Example usage:
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci number at position {n}:")
        print(f"Recursive: {fib_recursive(n)}")
        print(f"Iterative: {fib_iterative(n)}")
        print()
```

This script provides two functions to calculate the nth Fibonacci number: `fib_recursive` uses recursion, and `fib_iterative` uses iteration with memoization for improved performance. A `memoize` decorator is used to cache intermediate results, reducing the time complexity of the `fib_iterative` function. The example usage demonstrates the functionality of both functions.