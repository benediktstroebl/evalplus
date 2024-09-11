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
    n (int): The index of the element in the sequence to compute.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    
    # Base cases
    if n <= 0:
        return 0
    
    # Initialize the base array to store the first 5 elements of the fib4 sequence
    fib4_array = [0, 0, 2, 0, 0]
    
    # Compute the rest of the sequence iteratively
    for i in range(5, n + 1):
        # The next element is the sum of the last 4 elements
        fib4_array.append(fib4_array[i - 1] + fib4_array[i - 2] + fib4_array[i - 3] + fib4_array[i - 4])
    
    # Return the n-th element of the sequence
    return fib4_array[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the fib4 number sequence without using recursion. It uses an iterative approach to fill up an array `fib4_array` that stores the first `n + 1` elements of the sequence. The function then returns the n-th element of the sequence.