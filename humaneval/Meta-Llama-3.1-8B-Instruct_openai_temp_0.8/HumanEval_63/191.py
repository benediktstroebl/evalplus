```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the sequence
    sequence = [0, 0, 1] + [0] * (n - 2)

    # Compute the sequence
    for i in range(3, n + 1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]

    # Return the n-th element of the sequence
    return sequence[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that efficiently computes the n-th element of the FibFib number sequence. The function first checks the base cases and then initializes a list to store the sequence. It then iteratively computes the sequence using a loop and finally returns the n-th element. The test cases at the end demonstrate the function's correctness. 

The time complexity of this function is O(n), which is efficient for computing large elements of the sequence. However, it uses O(n) space to store the sequence, which may be a concern for very large values of n. If n is very large, a more space-efficient solution using recursion and memoization could be used. 

To implement this, you could use the following revised code:

```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize a dictionary to store the sequence
    sequence = {0: 0, 1: 0, 2: 1}

    # Compute the sequence
    for i in range(3, n + 1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]

    # Return the n-th element of the sequence
    return sequence[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(