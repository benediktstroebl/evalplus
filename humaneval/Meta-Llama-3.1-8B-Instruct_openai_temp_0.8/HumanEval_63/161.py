```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    :param n: The position of the element in the sequence.
    :return: The nth element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    else:
        memo = {0: 0, 1: 0, 2: 1}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses a dictionary `memo` to store previously computed values in the FibFib sequence. This approach is known as memoization and is used to avoid redundant computations and improve efficiency.