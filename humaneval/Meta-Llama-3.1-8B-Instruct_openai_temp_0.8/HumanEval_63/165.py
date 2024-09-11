### Efficient Fibonacci-like Sequence Implementation
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the number in the FibFib sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a dictionary to store previously computed values
        memo = {0: 0, 1: 0, 2: 1}
        
        # Define a helper function to perform the recursive computations
        def fibfib_helper(k):
            if k not in memo:
                memo[k] = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
            return memo[k]
        
        return fibfib_helper(n)

# Test cases
if __name__ == "__main__":
    print(fibfib(1))    # Expected: 0
    print(fibfib(5))    # Expected: 4
    print(fibfib(8))    # Expected: 24
```

This implementation uses a technique called memoization to store the results of expensive function calls and reuse them when the same inputs occur again. The `fibfib_helper` function performs the recursive computations, and the `memo` dictionary stores the previously computed values. This approach significantly reduces the computational overhead and makes the function more efficient for large values of `n`.