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

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize a list to store the first n+1 elements of the FibFib sequence
    fibfib_seq = [0, 0, 1] + [0]*(n-2)

    # Compute the first n elements of the FibFib sequence
    for i in range(3, n+1):
        fibfib_seq[i] = fibfib_seq[i-1] + fibfib_seq[i-2] + fibfib_seq[i-3]

    # Return the n-th element of the FibFib sequence
    return fibfib_seq[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

However, this solution has a time complexity of O(n) which can be improved to O(log n) by using memoization or dynamic programming.

Here is a more efficient solution using memoization:

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

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize a dictionary to store the first n+1 elements of the FibFib sequence
    memo = {0: 0, 1: 0, 2: 1}

    # Compute the first n elements of the FibFib sequence
    for i in range(3, n+1):
        if i-1 in memo and i-2 in memo and i-3 in memo:
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        else:
            raise ValueError("n is too large for memoization")

    # Return the n-th element of the FibFib sequence
    return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  #