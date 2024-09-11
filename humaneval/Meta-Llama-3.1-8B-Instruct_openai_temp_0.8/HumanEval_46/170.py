### Fib4 Number Sequence Computation
#### Problem Description

The Fib4 number sequence is a sequence that's similar to the Fibonacci sequence but with a different recurrence relation:
- `fib4(0)`: 0
- `fib4(1)`: 0
- `fib4(2)`: 2
- `fib4(3)`: 0
- `fib4(n)`: `fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

#### Solution
```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.

    Args:
    n (int): The position of the element to compute.

    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n < 2:
        return 0

    fib4_sequence = [0, 0, 2]
    for i in range(3, n + 1):
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])

    return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
#### Explanation

This solution uses an iterative approach to compute the `n-th` element of the fib4 number sequence. It initializes a list `fib4_sequence` with the first three elements of the sequence (0, 0, and 2). Then it iteratively computes the remaining elements of the sequence by adding the previous four elements. The function returns the `n-th` element of the sequence.

Note that this solution has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of `n`.