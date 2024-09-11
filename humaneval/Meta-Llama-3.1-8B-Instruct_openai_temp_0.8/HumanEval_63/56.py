```markdown
### FibFib Number Sequence Calculator

This Python script defines a function `fibfib(n)` to compute the n-th number in the FibFib number sequence.

#### Code
```python
def fibfib(n: int):
    """
    Compute the n-th number in the FibFib sequence.

    Args:
    n (int): The index of the number to compute. Must be a non-negative integer.

    Returns:
    int: The n-th number in the FibFib sequence.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    memo = {0: 0, 1: 0, 2: 1}  # Initialize a dictionary to store memoized values

    def fibfib_recursive(i: int) -> int:
        # If the value is already memoized, return it
        if i in memo:
            return memo[i]

        # Compute the value and store it in the memo dictionary
        memo[i] = fibfib_recursive(i-1) + fibfib_recursive(i-2) + fibfib_recursive(i-3)

        return memo[i]

    return fibfib_recursive(n)


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
#### Explanation

This script uses a recursive approach with memoization to efficiently compute the n-th number in the FibFib sequence.

1. The `fibfib(n)` function first checks if `n` is a non-negative integer and raises a `ValueError` if it's not.
2. It initializes a dictionary `memo` to store memoized values for previously computed numbers in the sequence.
3. The `fibfib_recursive(i)` function is a recursive helper function that computes the i-th number in the sequence.
4. If the value is already memoized, it returns the stored value.
5. Otherwise, it computes the value recursively and stores it in the memo dictionary.
6. Finally, the `fibfib(n)` function calls `fibfib_recursive(n)` to compute the n-th number in the sequence.

This script has a time complexity of O(n) and a space complexity of O(n) due to the memoization dictionary.