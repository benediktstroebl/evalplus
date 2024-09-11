```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the number in the sequence to compute.
    
    Returns:
    int: The nth element of the fib4 number sequence.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    if n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the first 4 elements of the sequence
    fib4_sequence = [0, 0, 2, 0]
    
    # Compute the rest of the sequence iteratively
    for i in range(4, n + 1):
        # Compute the next element as the sum of the previous 4 elements
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        # Append the new element to the sequence
        fib4_sequence.append(next_element)
    
    # Return the nth element of the sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4` that computes the nth element of the Fib4 number sequence using iteration and dynamic programming. It starts with the first 4 elements of the sequence (0, 0, 2, 0) and then iteratively computes the rest of the sequence by summing the previous 4 elements. The function raises a `ValueError` if the input is not a positive integer. The test cases at the end demonstrate the function's correctness.