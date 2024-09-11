```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element in the sequence to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```
This script uses a simple iterative approach to compute the n-th element of the FibFib number sequence. It uses a triple of variables `a`, `b`, and `c` to keep track of the last three elements in the sequence, updating them in each iteration. This approach has a time complexity of O(n), making it efficient for large values of `n`.