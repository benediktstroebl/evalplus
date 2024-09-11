```python
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


@memoize
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the FibFib sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script uses memoization to store the results of previously computed fibfib(n) values. This significantly reduces the computation time for n > 3 as it avoids redundant calculations. 

Please note that this function will raise a ValueError if n is a negative integer, as the problem statement does not define the behavior of the function for negative inputs.