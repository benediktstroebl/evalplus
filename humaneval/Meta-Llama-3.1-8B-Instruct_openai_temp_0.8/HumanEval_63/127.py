```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence,
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
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that computes the n-th element of the FibFib number sequence. The function uses a bottom-up dynamic programming approach to compute the sequence, where we store the last three elements of the sequence in the variables `a`, `b`, and `c`. We then iterate from `n=2` to `n=n`, updating these variables at each step to compute the next element of the sequence. The final result is stored in the variable `c`.

The script also includes a test section at the end, where we call the `fibfib(n)` function with the values `n=1`, `n=5`, and `n=8`, and print the results.