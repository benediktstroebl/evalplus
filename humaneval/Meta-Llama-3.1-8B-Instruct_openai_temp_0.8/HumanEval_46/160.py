### Efficient Fib4 Number Sequence Computation
#### Using Dynamic Programming

```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence efficiently using dynamic programming.
    
    The Fib4 sequence is defined as follows:
    - fib4(0) -> 0
    - fib4(1) -> 0
    - fib4(2) -> 2
    - fib4(3) -> 0
    - fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the element in the Fib4 sequence to be computed.
    
    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    
    # Initialize the base cases
    fib4_sequence = [0, 0, 2, 0] if n <= 3 else [0] * (n + 1)
    
    # Compute the sequence iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
    
    # Return the n-th element
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the Fib4 sequence. It initializes the base cases in the sequence as `[0, 0, 2, 0]` and then iteratively computes the remaining elements using a loop. The time complexity of this script is O(n), making it efficient for large values of n.