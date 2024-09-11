```python
def fibfib(n: int) -> int:
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
    ValueError: If n is negative.
    """

    # Check if n is negative and raise an error if it is
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0

    # Initialize a list to store the results of subproblems
    memo = [0, 0, 1] + [0]*(n-2)

    # Fill up the memo list using the recursive formula
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    # Return the n-th element of the FibFib sequence
    return memo[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

In this code, we use a technique called memoization to store the results of subproblems in a list called `memo`. This technique allows us to avoid recomputing the same values multiple times and greatly improves the efficiency of the function for large inputs. We also include some basic error checking to ensure that the input `n` is a non-negative integer.