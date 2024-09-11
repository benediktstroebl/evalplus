```markdown
## FibFib Number Sequence Computation
### Overview
The **FibFib** number sequence is similar to the Fibonacci sequence, but with a slightly modified recursive formula:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

### Implementation

```python
def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence.
    
    Args:
    n (int): The position of the element in the sequence to be computed.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the computed elements
    fibfib_sequence = [0, 0, 1]
    
    # Compute the sequence elements up to the nth element
    for i in range(3, n + 1):
        # Compute the next element as the sum of the previous three elements
        next_element = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        # Append the next element to the sequence
        fibfib_sequence.append(next_element)
    
    # Return the nth element
    return fibfib_sequence[n]
```

### Example Usage

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

Note: The above implementation uses a bottom-up dynamic programming approach to efficiently compute the n-th element of the FibFib number sequence. It stores the computed sequence elements in a list, which allows for faster computation of subsequent elements. This approach has a time complexity of O(n) and a space complexity of O(n), making it suitable for large values of n.