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
    
    This function computes the n-th element of the fib4 number sequence efficiently.
    
    Args:
    n (int): The index of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n < 4:
        # Base cases
        return [0, 0, 2][n]
    
    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Calculate the next elements in the sequence
    for _ in range(4, n+1):
        # Update the next four elements as the sum of the previous four
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the n-th element
    return d


# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses an iterative approach to compute the n-th element of the fib4 sequence. It maintains a list of the last four elements and updates them in each iteration. This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of n.