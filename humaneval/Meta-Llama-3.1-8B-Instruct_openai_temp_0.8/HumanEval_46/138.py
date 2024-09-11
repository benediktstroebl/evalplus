### Fib4 Number Sequence
#### Computing the n-th Element Efficiently

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Args:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n <= 1:  # Base cases
        return 0
    elif n == 2:  # Base case
        return 2
    elif n == 3:  # Base case
        return 0
    
    # Initialize a list to store the sequence elements
    sequence = [0, 0, 2, 0]
    
    # Compute the sequence iteratively
    for i in range(4, n + 1):
        # Calculate the next element as the sum of the previous four elements
        next_element = sequence[i - 1] + sequence[i - 2] + sequence[i - 3] + sequence[i - 4]
        
        # Append the next element to the sequence
        sequence.append(next_element)
    
    # Return the n-th element of the sequence
    return sequence[n]


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that computes the n-th element of the fib4 number sequence using an iterative approach. It handles base cases and uses a list to store the sequence elements, updating them iteratively until it reaches the desired element. The function then returns the n-th element of the sequence. The script includes test cases to demonstrate the correctness of the function.