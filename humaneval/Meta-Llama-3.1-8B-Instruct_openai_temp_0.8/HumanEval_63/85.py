```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the element in the fibfib sequence.

    Returns:
    int: The n-th element of the fibfib sequence.
    """
    if n < 0:
        raise ValueError("Negative arguments are not supported")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the results of subproblems
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 0
    memo[2] = 1

    # Fill up the memo list
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]


if __name__ == "__main__":
    # Test cases
    print(fibfib(1))    # Output: 0
    print(fibfib(5))    # Output: 4
    print(fibfib(8))    # Output: 24
```

This script uses memoization to efficiently compute the n-th element of the fibfib sequence. It initializes a list `memo` to store the results of subproblems and fills it up as needed, reducing the time complexity from exponential to linear.