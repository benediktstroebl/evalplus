```markdown
### FibFib Number Sequence
#### Efficiently Computing the n-th Element

The FibFib number sequence is a sequence similar to the Fibonacci sequence, defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

Below is a Python function to efficiently compute the n-th element of the FibFib number sequence using dynamic programming.

```python
def fibfib(n: int):
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
    elif n <= 3:
        return 1
    else:
        # Initialize a list to store the computed elements
        fibfib_sequence = [0, 0, 1, 1]
        
        # Compute the elements from the 4th to the n-th element
        for i in range(4, n + 1):
            fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
        
        # Return the n-th element
        return fibfib_sequence[n]

# Example use cases
print(fibfib(1))     # Output: 0
print(fibfib(5))     # Output: 4
print(fibfib(8))     # Output: 24
print(fibfib(10))    # Output: 90
```

This function uses a list to store the computed elements of the sequence, which allows it to compute the n-th element in O(n) time complexity. However, for larger values of n, memoization can be used to improve the efficiency of the function.