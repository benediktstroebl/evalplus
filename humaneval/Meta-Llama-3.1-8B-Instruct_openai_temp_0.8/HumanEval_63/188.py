```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The n-th number in the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases for the recursive formula
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the sequence
        sequence = [0, 0, 1] + [0]*(n-2)
        
        # Compute the sequence iteratively
        for i in range(3, n+1):
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]
        
        # Return the nth number in the sequence
        return sequence[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` that calculates the nth number in the FibFib sequence using a recursive formula. The function first checks if `n` is less than 0 and raises an error if it is. It then uses a list to store the sequence and calculates the nth number iteratively. Finally, it returns the nth number in the sequence.

This script also includes test cases to verify the correctness of the function. The test cases check the values of the function for `n = 1`, `n = 5`, and `n = 8`.