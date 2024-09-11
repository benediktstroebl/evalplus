### FibFib Number Sequence
#### A Python Function to Compute the n-th Element

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    but defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number sequence to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 2:
        return 0 if n == 1 else 1
    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

# Example usage:
if __name__ == "__main__":
    print(fibfib(1))   # Output: 0
    print(fibfib(5))   # Output: 4
    print(fibfib(8))   # Output: 24
```

This Python function `fibfib(n)` efficiently computes the n-th element of the FibFib number sequence using a simple iterative approach. It handles the base cases where `n` is less than or equal to 2, and then uses a loop to compute the remaining elements. The time complexity of this function is O(n), making it efficient for large values of `n`.