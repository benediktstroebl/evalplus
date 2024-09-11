```markdown
### FibFib Number Sequence
#### Computing the n-th Element Efficiently

The following Python script uses memoization to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int, memo: dict = {}):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the element in the sequence.
    memo (dict): A dictionary to store previously computed values. Defaults to {}.
    
    Returns:
    int: The n-th element in the FibFib number sequence.
    """
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Check if the value is already in the memo
    elif n in memo:
        return memo[n]
    # Otherwise, compute the value and store it in the memo
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        memo[n] = result
        return result

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

Note that this script uses a dictionary `memo` to store previously computed values, which allows it to avoid redundant computations and improve efficiency.
```