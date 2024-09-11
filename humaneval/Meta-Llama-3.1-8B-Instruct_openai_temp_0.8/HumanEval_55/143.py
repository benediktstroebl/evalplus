```markdown
### Fibonacci Sequence Calculator
#### Using Memoization for Efficient Calculation

Below is a Python script that calculates the nth Fibonacci number using memoization for efficient calculation.

```python
def memoize(func):
    """Decorator to store and reuse function results."""
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
    significantly improving performance for large inputs.
    
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
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script first defines a `memoize` decorator function to store and reuse function results. The `fib` function is then decorated with `@memoize` to enable memoization. This ensures that previously calculated Fibonacci numbers are stored and reused, significantly improving performance for large inputs.

Finally, the script includes an example usage section, where it calculates and prints the first 10 Fibonacci numbers.

### Running the Script
To run this script, save it to a file (e.g., `fibonacci.py`) and execute it using Python (e.g., `python fibonacci.py`). The output will be the first 10 Fibonacci numbers.