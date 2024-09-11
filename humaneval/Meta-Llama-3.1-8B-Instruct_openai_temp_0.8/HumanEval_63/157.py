```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The nth element of the FibFib number sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))   # Expected: 0
print(fibfib(5))   # Expected: 4
print(fibfib(8))   # Expected: 24
```

In this code, I've used a technique called "memoization" to store the results of expensive function calls and reuse them when the same inputs occur again. However, since the FibFib sequence is defined recursively with a small number of preceding elements, a simple iterative approach is more efficient in this case.