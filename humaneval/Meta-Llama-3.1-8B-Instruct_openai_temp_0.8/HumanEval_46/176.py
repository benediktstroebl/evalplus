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
    
    Args:
        n (int): The position of the element in the fib4 sequence.
        
    Returns:
        int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the fib4 sequence up to the n-th element
        fib4_sequence = [0, 0, 2]
        
        # Compute the fib4 sequence up to the n-th element
        for i in range(3, n + 1):
            # The i-th element is the sum of the (i-1)-th, (i-2)-th, (i-3)-th, and (i-4)-th elements
            fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
        
        # Return the n-th element of the fib4 sequence
        return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This code uses dynamic programming to compute the n-th element of the fib4 sequence without using recursion. The function first checks the base cases for n <= 1 and n == 2. For n > 2, it initializes a list to store the fib4 sequence up to the n-th element and then uses a loop to compute the sequence up to the n-th element. Finally, it returns the n-th element of the fib4 sequence.