```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position in the FibFib sequence to compute.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize the first three elements of the sequence
        a, b, c = 0, 0, 1
        
        # Compute the n-th element
        for _ in range(3, n + 1):
            a, b, c = b, c, b + c + a
        
        return c


# Test cases
if __name__ == "__main__":
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
```
This script uses an iterative approach to compute the n-th element of the FibFib sequence in O(n) time, where n is the input number. It initializes the first three elements of the sequence (a, b, c) and then iteratively updates them according to the recursive formula.