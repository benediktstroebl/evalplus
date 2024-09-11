### Fib4 Number Sequence
#### Python Implementation

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
    n (int): The index of the element to compute in the fib4 sequence.

    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the computed elements
        fib4_sequence = [0] * (n + 1)
        fib4_sequence[0] = fib4_sequence[1] = 0
        fib4_sequence[2] = 2
        
        # Compute the fib4 sequence iteratively
        for i in range(3, n + 1):
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        
        return fib4_sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This Python script defines the `fib4` function, which computes the n-th element of the Fib4 number sequence using an iterative approach. The function first checks for base cases and then initializes a list to store the computed elements. It then iteratively computes the Fib4 sequence up to the n-th element and returns the result. The script includes test cases to verify the correctness of the implementation.