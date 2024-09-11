### Fib4 Number Sequence Calculator
#### Python Implementation

```markdown
```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This implementation uses dynamic programming to efficiently compute the n-th element.

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the sequence iteratively
    for i in range(4, n + 1):
        # Calculate the next element as the sum of the previous four elements
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    return fib4_sequence[n]
```

### Usage

To use this implementation, simply call the `fib4(n)` function with the desired position `n` in the sequence:

```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This implementation has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.