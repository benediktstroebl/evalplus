### Self-Contained Python Script to Compute the n-th Element of the Fib4 Number Sequence

```markdown
# fib4.py

def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Args:
        n (int): The position of the element in the fib4 number sequence.
    
    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    
    # Handle edge cases where n is less than 0
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize the first four elements of the fib4 sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the n-th element of the fib4 sequence
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the n-th element of the fib4 sequence
    return d


# Test the fib4 function
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the fib4 number sequence using an iterative approach. The function handles edge cases where n is less than 0 and returns the correct results for the given test cases.