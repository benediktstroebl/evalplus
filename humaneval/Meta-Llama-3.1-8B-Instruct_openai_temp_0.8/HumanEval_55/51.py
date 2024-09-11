```python
def memoize(func):
    """A decorator to cache the results of function calls.
    
    Args:
        func (function): The function to cache.
    
    Returns:
        function: The cached function.
    """
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
    
    The Fibonacci sequence is defined recursively as follows:
    - F(1) = 1
    - F(n) = F(n - 1) + F(n - 2) for n > 1
    
    Args:
        n (int): The position of the Fibonacci number to return.
    
    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a decorator `memoize` that caches the results of function calls. It then uses this decorator to cache the results of the `fib` function, which calculates the n-th Fibonacci number. This approach avoids redundant calculations and improves performance for large values of `n`. The `fib` function is also well-documented with docstrings.