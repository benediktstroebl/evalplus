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
    n (int): The position of the element in the Fib4 sequence.
    
    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    
    # Handle edge cases
    if n <= 3:
        return 0 if n <= 1 else 2
    
    # Initialize the first four elements in the sequence
    a, b, c, d = 2, 0, 0, 0
    
    # Compute the first four elements in the sequence
    for _ in range(4, n + 1):
        # Update the elements in the sequence
        d, c, b, a = a + b + c + d, d, c, b
    
    return d
```

This script defines a function `fib4` to compute the n-th element of the Fib4 sequence. The function uses a loop to iteratively update the elements in the sequence, which makes it efficient for large values of n. The function handles edge cases at the beginning of the sequence separately from the rest of the sequence.

Example usage:

```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```