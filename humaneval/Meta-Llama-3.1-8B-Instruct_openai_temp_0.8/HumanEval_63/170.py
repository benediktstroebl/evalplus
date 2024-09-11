```markdown
### Fibonacci-like Sequence (FibFib) Computation
#### Efficiently Calculate the n-th Element of the FibFib Sequence

This script defines a function `fibfib` to compute the n-th element of the FibFib number sequence using dynamic programming.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 2:
        return 0
    if n == 3:
        return 1
    
    fibfib_sequence = [0, 0, 1]
    for i in range(3, n + 1):
        next_element = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        fibfib_sequence.append(next_element)
    
    return fibfib_sequence[n]


# Example usage
print(fibfib(1))   # 0
print(fibfib(5))   # 4
print(fibfib(8))   # 24
```

This script calculates the n-th element of the FibFib sequence by storing the previous elements in a list and using them to compute the next element. This approach has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.