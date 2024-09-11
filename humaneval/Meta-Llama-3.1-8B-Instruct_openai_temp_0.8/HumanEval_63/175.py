### Efficient Computation of FibFib Number Sequence
#### Using Memoization for Optimal Performance

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

    Example:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    memo = {0: 0, 1: 0, 2: 1}  # Initialize memoization dictionary

    def fibfib_helper(k: int) -> int:
        """
        Recursive helper function to compute the k-th element.
        """
        if k in memo:  # Check if result is already memoized
            return memo[k]
        result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
        memo[k] = result  # Memoize result
        return result

    return fibfib_helper(n)  # Compute and return the n-th element

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that uses memoization to efficiently compute the n-th element of the FibFib number sequence. The `fibfib_helper` function is a recursive helper function that computes the k-th element, and the `memo` dictionary stores the results of previously computed elements to avoid redundant calculations. The script includes example use cases to demonstrate the correctness of the function.