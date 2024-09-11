### Fib4 Number Sequence Computation

Below is a Python script that uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence.

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
        int: The n-th element of the Fib4 sequence.
    """
    if n <= 3:
        # Base cases
        fib4_sequence = [0, 0, 2]  # Initialize sequence with base cases
        return fib4_sequence[n]

    # Initialize a list to store the sequence up to the nth element
    sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        # Compute the next element as the sum of the previous four elements
        next_element = sequence[i - 1] + sequence[i - 2] + sequence[i - 3] + sequence[i - 4]
        # Append the next element to the sequence
        sequence.append(next_element)

    return sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a dynamic programming approach by precomputing the sequence up to the nth element and storing it in a list. This approach has a time complexity of O(n), which is more efficient than the recursive approach.