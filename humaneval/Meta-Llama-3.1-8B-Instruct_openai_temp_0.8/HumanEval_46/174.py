```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.
    
    The fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the element to compute.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    
    Example:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # Create an array to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0]*(n-3)

    # Use a loop to fill in the fib4 numbers
    for i in range(4, n+1):
        fib4_numbers[i] = fib4_numbers[i-1] + fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]

    # Return the n-th element of the fib4 number sequence
    return fib4_numbers[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function to compute the n-th element of the fib4 number sequence. It uses an array to store the previously computed fib4 numbers and then fills in the rest of the sequence using a loop. The function takes an integer `n` as input and returns the n-th element of the fib4 number sequence. The example usage at the end of the script tests the function with the provided test cases.