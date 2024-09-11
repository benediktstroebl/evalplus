### FibFib Sequence Calculator
#### A Python Script to Compute the n-th Element of the FibFib Number Sequence

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    This function efficiently computes the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element in the FibFib sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.

    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


# Example usage
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script defines the `fibfib` function, which uses a simple iterative approach to compute the n-th element of the FibFib sequence. The function takes an integer `n` as input and returns the corresponding element in the sequence. The example usage at the end demonstrates how to use the function to compute the first few elements of the sequence.