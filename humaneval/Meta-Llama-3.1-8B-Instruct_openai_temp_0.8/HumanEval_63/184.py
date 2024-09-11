```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the sequence.

    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a list to store the sequence and initialize the first three elements
        sequence = [0, 0, 1] + [0]*(n-2)

        # Compute the sequence from the 4-th element to the n-th element
        for i in range(3, n+1):
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]

        return sequence[n]


# Test the function
print(fibfib(1))      # 0
print(fibfib(5))      # 4
print(fibfib(8))      # 24
```

However, the above solution is not efficient for large inputs because it involves creating a list of size `n` and then iterating over it. If we want to improve the efficiency, we can use dynamic programming technique to store the sequence from the beginning and avoid unnecessary computations.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The index of the sequence.

    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    a, b, c = 0, 0, 1
    for i in range(3, n+1):
        a, b, c = b, c, a + b + c

    return c


# Test the function
print(fibfib(1))      # 0
print(fibfib(5))      # 4
print(fibfib(8))      # 24
```

This version of the function uses a constant amount of space and runs in O(n) time. It's suitable for large inputs.