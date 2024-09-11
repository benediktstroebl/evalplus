**FibFib Number Sequence**
==========================

Below is a Python function that efficiently computes the n-th element of the FibFib number sequence using dynamic programming.

```markdown
### fibfib Function
---------------

This function calculates the n-th element of the FibFib number sequence.
It uses dynamic programming to store and reuse previously computed values.

```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the element in the sequence.
    
    Returns:
        int: The n-th element of the FibFib sequence.
    """
    # Handle edge cases
    if n == 0 or n == 1:
        return 0
    
    # Create a dictionary to store previously computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    # Compute and store values up to the nth element
    for i in range(3, n + 1):
        # Calculate the i-th element using the recurrence relation
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    
    # Return the n-th element
    return memo[n]
```

### Example Usage
---------------

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This code first handles edge cases and initializes a dictionary `memo` to store previously computed values. It then computes and stores values up to the nth element using the recurrence relation, and finally returns the n-th element.