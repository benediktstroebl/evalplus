**Fib4 Number Sequence Calculator**
=====================================

Below is a Python script that efficiently calculates the n-th element of the Fib4 number sequence using dynamic programming.

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The index of the element to calculate in the Fib4 sequence.
        
    Returns:
        int: The n-th element of the Fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize the first four elements of the Fib4 sequence
    fib4_sequence = [0, 0, 2, 0]

    # Calculate the next elements in the sequence up to the nth element
    for i in range(4, n + 1):
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    # Return the nth element of the sequence
    return fib4_sequence[n]

# Example use cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a list to store the previously calculated elements of the Fib4 sequence, allowing it to efficiently calculate the nth element in O(n) time. The example use cases demonstrate how to use the `fib4` function to calculate the 5th, 6th, and 7th elements of the sequence.