```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Parameters:
    n (int): The position of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Initialize a list to store the fib4 sequence up to the nth element
    fib4_seq = [0, 0, 2, 0]
    
    # Compute the fib4 sequence up to the nth element
    for i in range(4, n + 1):
        # The next element is the sum of the last four elements
        fib4_seq.append(fib4_seq[i - 1] + fib4_seq[i - 2] + fib4_seq[i - 3] + fib4_seq[i - 4])
    
    # Return the nth element
    return fib4_seq[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```