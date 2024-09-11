```python
def memoize(func):
    """A simple memoizer to store the results of expensive function calls."""
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fib_fib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib_fib(0) == 0
    fib_fib(1) == 0
    fib_fib(2) == 1
    fib_fib(n) == fib_fib(n-1) + fib_fib(n-2) + fib_fib(n-3).
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_fib(n-1) + fib_fib(n-2) + fib_fib(n-3)


if __name__ == "__main__":
    print(fib_fib(1))  # Should print: 0
    print(fib_fib(5))  # Should print: 4
    print(fib_fib(8))  # Should print: 24
```

In this script, we first define a simple memoizer `memoize` that uses a dictionary to store the results of expensive function calls. This helps to avoid redundant calculations and makes the function much faster for larger inputs.

We then define the `fib_fib` function, which is the main function that computes the n-th element of the FibFib number sequence. We use the `memoize` decorator to memoize the `fib_fib` function.

The `if __name__ == "__main__":` block is used to test the `fib_fib` function with some example inputs. The `print` statements should print the expected results for the given inputs.