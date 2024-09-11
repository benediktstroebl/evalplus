### Fib4 Number Sequence
#### Efficient Computation of the n-th Element

Below is a Python function that uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence.

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """

    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize a list to store the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the sequence up to the n-th element
    for i in range(4, n + 1):
        # Update the sequence using the recurrence relation
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    # Return the n-th element
    return fib4_sequence[n]
```

#### Example Usage

```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This solution has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.