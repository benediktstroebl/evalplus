### Fib4 Number Sequence
#### Efficient Computation

Here's a Python script that uses dynamic programming to calculate the `n`-th element of the Fib4 number sequence efficiently:

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the element in the Fib4 sequence.
    
    Returns:
    int: The `n`-th element of the Fib4 sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the Fib4 sequence
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0] = fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    
    # Calculate the rest of the sequence
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
    
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script calculates the `n`-th element of the Fib4 sequence by creating a list to store the sequence up to `n` and then iterating over the list to calculate each element based on the previous four elements. This approach avoids the recursion and is significantly more efficient for large values of `n`.