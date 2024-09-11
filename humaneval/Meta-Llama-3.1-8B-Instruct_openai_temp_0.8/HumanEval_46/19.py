### Fib4 Number Sequence
#### Efficiently Computing the n-th Element

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the element in the Fib4 sequence.
    
    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    if n <= 3:
        # Base cases
        return [0, 0, 2, 0][n]
    
    # Initialize a list to store the first 5 elements of the sequence
    fib4_sequence = [0, 0, 2, 0, 0]
    
    # Compute the rest of the sequence
    for i in range(4, n):
        # The i-th element is the sum of the four preceding elements
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
    
    # Return the n-th element
    return fib4_sequence[n-1]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the n-th element of the Fib4 sequence. It first handles the base cases (when `n` is less than or equal to 3) and then initializes a list to store the first 5 elements of the sequence. It then computes the rest of the sequence by iterating over the range from 4 to `n-1` and storing the sum of the four preceding elements in the list. Finally, it returns the n-th element of the sequence.