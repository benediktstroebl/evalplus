```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the sequence.
    
    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        # Initialize an array to store the sequence
        fibfib_sequence = [0, 0, 1, 2]
        
        # Compute the sequence up to the nth element
        for i in range(4, n + 1):
            fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])
        
        # Return the nth element
        return fibfib_sequence[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

The time complexity of this solution is O(n), where n is the input number. This is because we are computing the sequence up to the nth element. The space complexity is also O(n), as we are storing the sequence in an array.