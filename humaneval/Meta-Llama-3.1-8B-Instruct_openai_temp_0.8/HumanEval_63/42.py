```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the FibFib number sequence.

    Raises:
        ValueError: If n is less than 0.
    """

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Memoization to store previously computed values
        memo = {0: 0, 1: 0, 2: 1}

        # Compute the nth element using memoization
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

        return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses memoization to efficiently store previously computed values of the sequence. This approach avoids redundant calculations, making the function more efficient for larger values of n.