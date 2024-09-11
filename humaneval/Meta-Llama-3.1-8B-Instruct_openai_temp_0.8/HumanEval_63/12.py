```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    Args:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the sequence elements
    fibfib_sequence = [0, 0, 1]
    
    # Generate the sequence elements up to the n-th element
    for i in range(3, n + 1):
        next_element = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        fibfib_sequence.append(next_element)
    
    # Return the n-th element
    return fibfib_sequence[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

However, this solution is inefficient for large values of `n` as it stores the entire sequence in memory. We can use dynamic programming to only store the last three elements of the sequence, reducing the memory usage.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    Args:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the last three sequence elements
    last_three_elements = [0, 0, 1]
    
    # Generate the sequence elements up to the n-th element
    for i in range(3, n + 1):
        next_element = last_three_elements[0] + last_three_elements[1] + last_three_elements[2]
        last_three_elements[0] = last_three_elements[1]
        last_three_elements[1] = last_three_elements[2]
        last_three_elements[2] = next_element
    
    # Return the n-th element
    return last_three_elements[2]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```