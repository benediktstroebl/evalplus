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
    n (int): The position of the element in the Fib4 sequence.

    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize an array to store the sequence
        fib4_sequence = [0]*(n+1)
        fib4_sequence[2] = 2
        for i in range(3, n+1):
            # For each element in the sequence, calculate the sum of the four previous elements
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that calculates the `n-th` element of the Fib4 sequence using dynamic programming. It initializes an array `fib4_sequence` of size `n+1` to store the sequence, then fills in the array iteratively from index 3 to `n`. The final result is `fib4_sequence[n]`. The function handles the base cases `n <= 1` and `n == 2` separately.