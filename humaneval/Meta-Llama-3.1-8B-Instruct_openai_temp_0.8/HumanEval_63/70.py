**FibFib Number Sequence Calculator**
=====================================

Below is a Python script that efficiently computes the n-th element of the FibFib number sequence.

```python
from functools import lru_cache

def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    @lru_cache(maxsize=None)
    def fibfib_recursive(k):
        if k < 0:
            raise ValueError("k must be a non-negative integer")
        elif k == 0 or k == 1:
            return 0
        elif k == 2:
            return 1
        else:
            return fibfib_recursive(k-1) + fibfib_recursive(k-2) + fibfib_recursive(k-3)
    
    return fibfib_recursive(n)

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

The `fibfib` function uses memoization to efficiently compute the n-th element of the FibFib number sequence. The `lru_cache` decorator from the `functools` module is used to cache the results of expensive function calls and reuses them when the same inputs occur again.

Note that the recursive version of the function is only used for indices beyond 2, and the results are cached to avoid redundant computations.