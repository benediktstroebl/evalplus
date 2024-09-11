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
    
    :param n: The position of the element in the Fib4 sequence.
    :return: The n-th element of the Fib4 sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the sequence
    fib4_seq = [0, 0, 2, 0] + [0]*(n-3)
    
    # Compute the sequence in O(n) time complexity
    for i in range(4, n+1):
        fib4_seq[i-1] = fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4]
    
    return fib4_seq[n-1]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a top-down approach to compute the n-th element of the Fib4 sequence. It first initializes a list with the base cases and then iteratively computes the rest of the sequence in O(n) time complexity. This approach avoids the O(2^n) complexity of recursive solutions and is more efficient for large values of n.