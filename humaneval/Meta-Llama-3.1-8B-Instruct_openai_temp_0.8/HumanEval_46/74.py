```markdown
### Fib4 Number Sequence
#### A Self-Contained Python Script

This script efficiently computes the n-th element of the fib4 number sequence using dynamic programming. 

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the fib4 sequence.

    Returns:
        int: The value of the n-th element in the fib4 sequence.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n <= 3:
        return [0, 0, 2][n]
    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to store the previously computed values in the `fib4_sequence` list, avoiding the redundant computation required by recursive function calls. The function returns the value at index `n` in the `fib4_sequence` list.