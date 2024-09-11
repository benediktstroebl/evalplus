### FibFib Number Sequence Computation
#### Using Dynamic Programming for Efficient Computation

The following Python script utilizes dynamic programming to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the desired element in the sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed values
    fibfib_values = [0] * (n + 1)
    fibfib_values[1] = 0
    fibfib_values[2] = 1

    # Compute the values using dynamic programming
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]

    return fibfib_values[n]

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

In this code:

1.  We first handle the base cases for `n <= 1` and `n == 2`.
2.  We initialize a list `fibfib_values` to store the computed values.
3.  We use dynamic programming to compute the values iteratively, starting from `i = 3`.
4.  Finally, we return the computed value for the `n-th` element.

This approach has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of `n`.