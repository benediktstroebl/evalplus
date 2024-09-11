```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Parameters:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n == 0 or n == 1:
        # Base case: fib4(0) and fib4(1) are 0
        return 0
    elif n == 2:
        # Base case: fib4(2) is 2
        return 2
    elif n == 3:
        # Base case: fib4(3) is 0
        return 0
    
    # Initialize the first four elements of the fib4 sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the nth element of the fib4 sequence
    for _ in range(4, n + 1):
        # Update the four previous elements
        a, b, c, d = b, c, d, a + b + c + d
    
    return d


# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This Python script defines a function `fib4(n)` to efficiently compute the n-th element of the Fib4 number sequence. It uses a loop to compute the nth element without using recursion. The function is tested with the provided test cases.