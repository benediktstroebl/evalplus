```markdown
### Fibonacci-like Sequence (FibFib)
#### Problem Description
The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

#### Solution
```python
def fibfib(n: int):
    """
    Compute the n-th element in the FibFib number sequence.

    Args:
    n (int): The index of the element in the sequence.

    Returns:
    int: The n-th element in the FibFib sequence.
    """
    if n <= 1:
        # Base cases
        return 0 if n == 1 else 0
    elif n == 2:
        # Base case
        return 1
    else:
        # Initialize a list to store the sequence
        fibfib_sequence = [0, 0, 1] + [0] * (n - 2)
        
        # Compute the sequence iteratively
        for i in range(3, n + 1):
            fibfib_sequence[i] = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        
        # Return the n-th element
        return fibfib_sequence[n]

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This script defines a function `fibfib` that computes the n-th element in the FibFib number sequence using dynamic programming. It uses a list to store the sequence and iteratively computes the elements from the 3rd to the n-th. The base cases are handled directly in the function.