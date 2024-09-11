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
    n (int): The position of the element in the Fib4 sequence.
    
    Returns:
    int: The n-th element of the Fib4 sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the Fib4 sequence
    fib4_seq = [0, 0, 2, 0]
    
    # Generate the Fib4 sequence up to the n-th element
    for i in range(4, n + 1):
        # Calculate the next element as the sum of the previous four elements
        next_element = fib4_seq[i - 1] + fib4_seq[i - 2] + fib4_seq[i - 3] + fib4_seq[i - 4]
        # Append the next element to the sequence
        fib4_seq.append(next_element)
    
    # Return the n-th element of the Fib4 sequence
    return fib4_seq[n]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```