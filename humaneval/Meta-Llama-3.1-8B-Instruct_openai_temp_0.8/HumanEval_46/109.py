Here's a Python solution using dynamic programming to efficiently compute the n-th element of the fib4 number sequence:

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
    n (int): The position of the element in the fib4 number sequence.

    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n <= 0:
        return 0
    
    # Initialize a list to store the computed elements of the fib4 sequence
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    
    # Compute the elements of the fib4 sequence in a bottom-up manner
    for i in range(2, n + 1):
        if i == 2:
            fib4_sequence[i] = 2
        elif i == 3:
            fib4_sequence[i] = 0
        else:
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This solution uses a bottom-up dynamic programming approach to efficiently compute the n-th element of the fib4 number sequence. It initializes a list to store the computed elements of the fib4 sequence and then iteratively computes each element based on the previously computed elements. This approach avoids the use of recursion and reduces the time complexity of the computation.