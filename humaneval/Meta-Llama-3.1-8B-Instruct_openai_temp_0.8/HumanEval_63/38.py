```python
def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the element in the sequence to compute.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the sequence
    sequence = [0, 0, 1] + [0]*(n-2)
    
    # Compute the sequence iteratively
    for i in range(3, n+1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]
    
    return sequence[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines the `fibfib` function that efficiently computes the n-th element of the FibFib number sequence. It uses a list to store the sequence and iteratively computes the elements from the 3rd to the n-th. The function also includes base cases for n = 0, 1, and 2. The script includes test cases to verify the correctness of the function.