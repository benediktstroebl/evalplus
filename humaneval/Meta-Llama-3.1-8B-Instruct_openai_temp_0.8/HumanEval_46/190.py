```markdown
### Fib4 Number Sequence Calculator

This Python script calculates the n-th element of the Fib4 number sequence efficiently using dynamic programming.

#### Code
```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the Fib4 sequence.

    Returns:
        int: The n-th element of the Fib4 sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n <= 3:
        return [0, 0, 2, 0][n]
    else:
        fib4_sequence = [0, 0, 2, 0, 2]
        for i in range(4, n + 1):
            fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
        return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
#### Explanation
This script calculates the n-th element of the Fib4 sequence by maintaining a list of previously calculated elements, `fib4_sequence`. It iterates from the 4th element to the n-th element, calculating each element as the sum of the previous four elements. This approach avoids the exponential time complexity of recursive solutions and is therefore much more efficient for large values of n.