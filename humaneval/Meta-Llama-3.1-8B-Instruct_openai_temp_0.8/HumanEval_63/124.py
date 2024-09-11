```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 3:  # Base cases already covered
        return None

    # Initialize a list to store the computed values
    fibfib_values = [0, 0, 1] + [None] * (n - 2)

    # Compute the values iteratively
    for i in range(3, n + 1):
        if fibfib_values[i - 1] is not None and fibfib_values[i - 2] is not None and fibfib_values[i - 3] is not None:
            fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]

    return fibfib_values[n]


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

However, a more efficient solution can be achieved by using dynamic programming with constant space. Here is the improved version of the code:

```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 2:
        return 0 if n <= 1 else 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, b + c + a

    return c


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this improved version, the function uses only three variables `a`, `b`, and `c` to store the last three numbers in the sequence, thus reducing the space complexity to O(1).