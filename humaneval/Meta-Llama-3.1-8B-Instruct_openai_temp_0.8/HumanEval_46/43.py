### Fibonacci-like Sequence (Fib4)
#### Computing the n-th element without recursion

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
        n (int): The index of the sequence element to compute.

    Returns:
        int: The nth element of the Fib4 sequence.
    """
    if n <= 3:
        return [0, 0, 2, 0][n]
    
    # Initialize an array to store the sequence values
    fib4_sequence = [0, 0, 2, 0, 0] * (n // 4 + 1)
    
    # Compute the sequence elements iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    # Return the nth element
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that efficiently computes the nth element of the Fib4 sequence without using recursion. The approach involves initializing an array to store the sequence values and then computing them iteratively using a loop. The result is returned at the end of the function. The test cases provided verify the correctness of the implementation.