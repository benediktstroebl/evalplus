```python
def fibfib(n: int):
    """
    Computes the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib` that takes an integer `n` as input and returns the n-th element of the FibFib number sequence. It uses a loop to iteratively compute the sequence elements, starting from the base cases `fibfib(0)` and `fibfib(1)`. The function is then tested with the provided test cases.