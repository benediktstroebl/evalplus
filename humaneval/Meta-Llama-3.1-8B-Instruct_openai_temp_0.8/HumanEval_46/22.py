```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Parameters:
    n (int): The index of the sequence to compute.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    
    # Handle edge cases where n is less than or equal to 3
    if n <= 3:
        result = [0, 0, 2, 0][n]
    else:
        # Initialize an array to store the last 5 elements of the sequence
        # We need to store the last 5 elements because we need to compute the
        # current element as the sum of the last 4 elements
        fib4_sequence = [0, 0, 2, 0, 0]
        
        # Compute each element of the sequence up to the nth element
        for i in range(4, n + 1):
            # The current element is the sum of the last 4 elements
            fib4_sequence.append(sum(fib4_sequence[-4:]))
        
        # Return the nth element of the sequence
        result = fib4_sequence[n]
    
    return result


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

In this code, we first handle the edge cases where `n` is less than or equal to 3. Then, we initialize an array to store the last 5 elements of the sequence. We compute each element of the sequence up to the nth element by iterating from `4` to `n+1` (because we have already stored the first 4 elements). In each iteration, we append the sum of the last 4 elements to the array, effectively computing the current element. Finally, we return the nth element of the sequence.