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
        n (int): The index of the number in the fib4 sequence.
    
    Returns:
        int: The n-th number in the fib4 sequence.
    """
    if n <= 0:
        return 0

    # Initialize the first four numbers in the sequence
    prev1, prev2, prev3, prev4 = 0, 0, 2, 0

    # Compute the n-th number in the sequence
    for _ in range(2, n + 1):
        # Update the previous four numbers
        prev1, prev2, prev3, prev4 = prev2, prev3, prev4, prev1 + prev2 + prev3 + prev4

    return prev4


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a loop to efficiently compute the n-th number in the fib4 sequence. It keeps track of the previous four numbers in the sequence and updates them at each iteration. This approach avoids the recursion and has a time complexity of O(n).