```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Parameters:
    n (int): The index of the FibFib number to compute.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
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

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This function uses a simple iterative approach to compute the n-th element of the FibFib sequence. It starts with the base cases for n <= 2 and then uses a loop to compute the rest of the sequence from right to left. The `a, b, c` variables are used to store the last three computed elements, and at each iteration, they are updated with the next three elements in the sequence.

This approach has a time complexity of O(n), which is efficient for computing large values of n. However, please note that the FibFib sequence grows very rapidly, and large values of n may exceed the maximum value that can be represented by an integer in Python.