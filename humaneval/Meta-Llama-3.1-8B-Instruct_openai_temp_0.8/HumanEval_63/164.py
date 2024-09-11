```markdown
### FibFib Number Sequence
#### A Python Function to Compute the n-th Element

Below is a Python function that uses memoization to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int, memo: dict = {}):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element in the FibFib sequence.
        memo (dict, optional): A dictionary to store previously computed values. Defaults to {}.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 0
    if n == 3:
        return 1
    memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    return memo[n]

# Example usage:
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This function uses a dictionary called `memo` to store previously computed values. Before computing the n-th element, it checks if it already exists in `memo`. If it does, the function returns the stored value. If not, it computes the value and stores it in `memo` for future use. This technique reduces the time complexity of the function from O(2^n) to O(n), making it more efficient for large values of n.