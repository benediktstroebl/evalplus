```python
def fib4(n: int) -> int:
    """
    This function calculates the n-th element of the Fib4 number sequence.
    
    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Parameters:
    n (int): The position of the element in the Fib4 number sequence.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    # Initialize a list to store the numbers in the sequence
    fib4_sequence = [0, 0, 2, 0]
    
    # Calculate the elements in the sequence up to the n-th element
    for i in range(4, n + 1):
        # Calculate the next element as the sum of the previous four elements
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        # Append the next element to the sequence
        fib4_sequence.append(next_element)
    
    # Return the n-th element of the sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4` that calculates the n-th element of the Fib4 number sequence. It uses an iterative approach to calculate the elements in the sequence up to the n-th element. The function takes an integer `n` as input and returns the n-th element of the sequence. The script also includes test cases to verify that the function works correctly.