```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.
    
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    fib_sequence = [0, 0, 2, 0]
    
    for i in range(4, n + 1):
        # Compute the next element as the sum of the four previous elements
        next_element = fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3] + fib_sequence[i - 4]
        fib_sequence.append(next_element)
    
    return fib_sequence[n]
```

You can test this function with the provided examples:
```markdown
# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```