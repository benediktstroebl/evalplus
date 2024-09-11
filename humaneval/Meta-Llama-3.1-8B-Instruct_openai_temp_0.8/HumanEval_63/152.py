```python
def memoized_fibfib(n: int, memo: dict = {0: 0, 1: 0, 2: 1}) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.
        memo (dict): A dictionary used for memoization. Defaults to {0: 0, 1: 0, 2: 1}.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n not in memo:
        memo[n] = memoized_fibfib(n-1, memo) + memoized_fibfib(n-2, memo) + memoized_fibfib(n-3, memo)
    return memo[n]

def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    return memoized_fibfib(n)

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a recursive function `memoized_fibfib` with memoization to efficiently compute the n-th element of the fibfib number sequence. The `fibfib` function is a wrapper around `memoized_fibfib` for simplicity. The test cases at the end demonstrate the functionality of the `fibfib` function.