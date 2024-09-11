```markdown
### Fib4 Number Sequence
#### A Python Script to Compute the nth Element of the Fib4 Sequence

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the Fib4 sequence.

    Returns:
        int: The nth element of the Fib4 sequence.

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

    # Initialize a list to store the Fibonacci sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the Fibonacci sequence up to the nth element
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])

    # Return the nth element
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines a function `fib4` that computes the nth element of the Fib4 sequence using memoization, which stores the computed Fibonacci numbers in a list and reuses them when needed. The function handles edge cases and invalid inputs, and includes docstrings and test cases to ensure correctness.