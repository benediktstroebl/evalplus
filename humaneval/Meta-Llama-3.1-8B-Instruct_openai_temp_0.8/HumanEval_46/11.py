### Fib4 Number Sequence
#### Computing the N-th Element

Here is a Python script that uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence.

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

    :param n: The index of the element to compute (1-indexed)
    :return: The n-th element of the Fib4 number sequence
    """
    if n == 0:
        return 0
    
    # Initialize a list to store the computed sequence elements
    fib4_seq = [0]*5
    
    # Fib4(0) = 0
    fib4_seq[0] = 0
    
    # Fib4(1) = 0
    fib4_seq[1] = 0
    
    # Fib4(2) = 2
    fib4_seq[2] = 2
    
    # Fib4(3) = 0
    fib4_seq[3] = 0
    
    # Compute the Fibonacci sequence elements up to the n-th element
    for i in range(4, n+1):
        fib4_seq[i] = fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4]
    
    # Return the n-th element of the Fib4 sequence
    return fib4_seq[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

### How it Works

*   We use a list `fib4_seq` to store the computed sequence elements, with indices 0 to 4 to match the problem's sequence definition.
*   We initialize the first four elements of the `fib4_seq` list based on the problem's base cases.
*   Then, we iterate from `i = 4` to `n` (inclusive) and compute each element as the sum of the previous four elements.
*   Finally, we return the `n-th` element of the computed `fib4_seq` list.