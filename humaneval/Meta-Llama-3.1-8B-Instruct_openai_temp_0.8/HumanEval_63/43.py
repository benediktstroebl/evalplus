```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows: 
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a dictionary to store previously computed values
        memo = {0: 0, 1: 0, 2: 1}
        for i in range(3, n + 1):
            # Compute the i-th element as the sum of the three preceding elements
            memo[i] = memo.get(i - 1, 0) + memo.get(i - 2, 0) + memo.get(i - 3, 0)
        return memo[n]

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses a dictionary called `memo` to store previously computed values of the FibFib sequence. This approach is known as memoization, which helps to avoid redundant computations and improve the performance of the function.