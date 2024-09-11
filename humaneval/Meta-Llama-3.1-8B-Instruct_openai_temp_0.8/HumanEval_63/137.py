```python
def memoize(func):
    """A decorator to memoize the results of a function."""
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


@memoize
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
```

However, using recursion for large inputs may exceed the maximum recursion depth due to Python's recursion limit and also be inefficient due to repeated computation. We can use dynamic programming to solve this problem more efficiently. Here is a revised version:

```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    
    fib_prev_prev_prev = 0
    fib_prev_prev = 0
    fib_prev = 1
    
    for _ in range(2, n):
        fib_current = fib_prev_prev_prev + fib_prev_prev + fib_prev
        
        # Update previous values
        fib_prev_prev_prev = fib_prev_prev
        fib_prev_prev = fib_prev
        fib_prev = fib_current
    
    return fib_prev
```