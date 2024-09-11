```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the FibFib sequence.

    Returns:
        int: The nth number in the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first three numbers in the sequence
    a, b, c = 0, 0, 1
    
    # Compute the nth number in the sequence
    for _ in range(3, n + 1):
        # Update the numbers in the sequence
        a, b, c = b, c, b + c + a
    
    # Return the nth number in the sequence
    return c


# Test cases
if __name__ == "__main__":
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` that efficiently computes the nth number in the FibFib sequence. It uses a loop to compute the sequence up to the nth number, rather than recursively computing each number from scratch. This makes the function more efficient and less prone to stack overflows for large values of n.