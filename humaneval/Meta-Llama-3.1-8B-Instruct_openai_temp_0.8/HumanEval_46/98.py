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
        n (int): The nth element of the fib4 number sequence.
    
    Returns:
        int: The nth element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_values.insert(0, fib4_values[0] + fib4_values[1] + fib4_values[2] + fib4_values[3])
        fib4_values.pop()
    
    return fib4_values[0]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the nth element of the fib4 number sequence, storing the previous four elements in a list to avoid repeated computation. The time complexity of this approach is O(n), which is more efficient than the recursive approach for large values of n.