### Self-Contained Python Script
```markdown
### Fib4 Number Sequence

The Fib4 number sequence is a sequence similar to the Fibonacci sequence, 
defined as follows:

* `fib4(0)` -> 0
* `fib4(1)` -> 0
* `fib4(2)` -> 2
* `fib4(3)` -> 0
* `fib4(n)` -> `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)`

Below is a Python function that efficiently computes the n-th element of the fib4 number sequence without using recursion.

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.

    Args:
    n: An integer representing the position in the sequence.

    Returns:
    An integer representing the n-th element of the fib4 sequence.
    """
    # Handle edge cases
    if n <= 0:
        return 0
    # Handle base case
    elif n == 2:
        return 2
    # Handle base case
    elif n == 3:
        return 0
    # Initialize variables to store the last four numbers in the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the n-th element using dynamic programming
    for _ in range(4, n + 1):
        # Update the last four numbers in the sequence
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the n-th element
    return d


# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script provides an efficient solution to compute the n-th element of the fib4 number sequence using dynamic programming. It uses a loop to iteratively update the last four numbers in the sequence, reducing the time complexity to O(n).