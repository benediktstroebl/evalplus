### Fibonacci Number Generator
#### Using Memoization to Optimize Performance

Below is a Python script that implements a Fibonacci number generator using memoization to optimize performance. Memoization is a technique that stores the results of expensive function calls so that they can be reused instead of recalculated.

```markdown
### fibonacci.py

```python
def memoize(func):
    """Decorator to store the results of expensive function calls."""
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
    return fib(n - 1) + fib(n - 2)


# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script defines a `memoize` decorator to store the results of expensive function calls. The `fib` function is decorated with `memoize` to optimize its performance by storing the results of previous Fibonacci calculations.

### Running the Script
To run the script, save it to a file named `fibonacci.py` and execute it using Python:

```bash
python fibonacci.py
```

This will print the 10th, 1st, and 8th Fibonacci numbers to the console.