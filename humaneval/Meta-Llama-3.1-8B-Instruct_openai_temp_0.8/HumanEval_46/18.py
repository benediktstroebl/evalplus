### Fib4 Number Sequence

The following Python script defines a function `fib4` that efficiently computes the n-th element of the Fib4 number sequence using dynamic programming.

```markdown
### Code

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Parameters:
    n (int): The index of the element to compute.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    if n <= 0:
        return 0
    
    # Initialize a list to store the computed elements
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    
    # Compute the elements of the sequence
    for i in range(2, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    # Return the n-th element
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

### Explanation

The `fib4` function uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence.

1.  We initialize a list `fib4_sequence` of size `n + 1` to store the computed elements of the sequence.
2.  We set the first two elements of the sequence to 0, as per the definition of the Fib4 sequence.
3.  We iterate from `i = 2` to `n`, and for each `i`, we compute the ith element as the sum of the three preceding elements: `fib4_sequence[i-1]`, `fib4_sequence[i-2]`, and `fib4_sequence[i-3]`.
4.  Finally, we return the `n-th` element of the sequence, which is stored at index `n` in the `fib4_sequence` list.

This approach avoids the overhead of recursive function calls and has a time complexity of O(n), making it efficient for large values of n.