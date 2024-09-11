```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    This function efficiently computes the n-th element of the fibfib number sequence using memoization.

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 3:
        return 0

    # Create a dictionary to store the memoized results
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_memoized(k: int) -> int:
        """
        Helper function to compute the k-th element of the fibfib number sequence using memoization.

        Args:
            k (int): The index of the FibFib number to compute.

        Returns:
            int: The k-th element of the fibfib number sequence.
        """
        # If the result is already memoized, return it
        if k in memo:
            return memo[k]

        # Otherwise, compute the result and store it in the memo dictionary
        result = fibfib_memoized(k - 1) + fibfib_memoized(k - 2) + fibfib_memoized(k - 3)
        memo[k] = result
        return result

    return fibfib_memoized(n)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24

```

This script defines a function `fibfib` that efficiently computes the n-th element of the fibfib number sequence using memoization. The function first checks for the base cases, and then uses a helper function `fibfib_memoized` to compute the result using memoization. The test cases are used to verify the correctness of the function.