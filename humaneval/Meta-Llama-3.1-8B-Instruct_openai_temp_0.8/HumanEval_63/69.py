```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """

    # Create a dictionary to store the computed elements for memoization
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_helper(k: int) -> int:
        # If the element is already computed, return it directly
        if k in memo:
            return memo[k]

        # If the element is not computed, compute it and store it in the dictionary
        memo[k] = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
        return memo[k]

    # Call the helper function to compute the n-th element
    return fibfib_helper(n)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this script, we use a technique called memoization to store the computed elements of the FibFib sequence in a dictionary. This allows us to avoid redundant computations and improve the efficiency of the function. The `fibfib_helper` function is the recursive helper function that computes the elements of the sequence, and the `fibfib` function is the main function that calls the helper function.