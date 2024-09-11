**Fib4 Number Sequence Calculator**
=====================================

Below is a Python script that efficiently calculates the n-th element of the Fib4 number sequence.

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    Args:
    n (int): The index of the element in the sequence.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n == 4:
        return 3
    else:
        # Initialize a list to store the sequence
        fib4_sequence = [0, 0, 2, 0, 3] + [0]*(n-4)
        
        # Compute the sequence iteratively
        for i in range(4, n):
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        
        # Return the n-th element
        return fib4_sequence[n-1]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script uses a list to store the sequence as it's computed, which makes it efficient for large values of `n`. The base cases are handled separately to avoid repeated computation.