```markdown
### Fib4 Number Sequence

#### Problem Description

The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- `fib4(0)` -> `0`
- `fib4(1)` -> `0`
- `fib4(2)` -> `2`
- `fib4(3)` -> `0`
- `fib4(n)` -> `fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`.

#### Solution

We can use dynamic programming to efficiently compute the `n-th` element of the `fib4` number sequence without using recursion.

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the element in the Fib4 sequence to be computed.

    Returns:
    int: The n-th element of the Fib4 sequence.
    """

    # Handle edge cases where n is less than 4
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the first 4 elements of the Fib4 sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the n-th element of the Fib4 sequence
    for i in range(4, n + 1):
        # The i-th element is the sum of the (i-1)-th, (i-2)-th, (i-3)-th, and (i-4)-th elements
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])

    # Return the n-th element
    return fib4_sequence[n]


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that uses dynamic programming to compute the `n-th` element of the Fib4 sequence. The function initializes a list to store the first 4 elements of the sequence and then computes the remaining elements iteratively. Finally, the function returns the `n-th` element of the sequence. The script includes test cases to demonstrate the function's correctness.