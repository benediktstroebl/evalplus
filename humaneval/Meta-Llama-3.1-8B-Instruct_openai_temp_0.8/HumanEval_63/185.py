```python
def memoized_fibfib(n: int, memo: dict = {}):
    """The memoized FibFib number sequence is a sequence similar to the FibFib sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    This function uses memoization to efficiently compute the n-th element of the fibfib number sequence.

    Args:
        n (int): The position of the element to compute in the fibfib sequence.
        memo (dict): A dictionary to store previously computed values. Defaults to {}.

    Returns:
        int: The n-th element of the fibfib sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = memoized_fibfib(n-1, memo) + memoized_fibfib(n-2, memo) + memoized_fibfib(n-3, memo)
        memo[n] = result
        return result

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the FibFib sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    This function efficiently computes the n-th element of the fibfib number sequence.

    Args:
        n (int): The position of the element to compute in the fibfib sequence.

    Returns:
        int: The n-th element of the fibfib sequence.
    """
    return memoized_fibfib(n)

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a two-function approach. The inner function `memoized_fibfib` is a recursive function with memoization, which stores previously computed values in a dictionary to avoid redundant computations. The outer function `fibfib` is the main function that calls `memoized_fibfib` to efficiently compute the n-th element of the fibfib sequence.