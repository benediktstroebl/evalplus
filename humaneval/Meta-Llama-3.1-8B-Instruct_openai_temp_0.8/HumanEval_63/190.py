### FibFib Number Sequence
#### A Python Solution

Here is a Python function that efficiently computes the n-th element of the FibFib number sequence using memoization to avoid redundant calculations.

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibbonacci sequence,
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """

    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize a dictionary to store the computed values
    memo = {0: 0, 1: 0, 2: 1}

    # Compute the n-th element using memoization
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    return memo[n]
```

This function uses a dictionary to store the computed values and avoid redundant calculations, making it efficient for large values of `n`. It also includes input validation and docstrings to provide clear documentation and usage guidelines.