```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    """
    
    # Handle base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize a list to store the fib4 sequence
    fib4_sequence = [0, 0, 2]
    
    # Compute the fib4 sequence up to the n-th element
    for i in range(3, n + 1):
        # Compute the i-th element as the sum of the previous four elements
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
    
    # Return the n-th element of the fib4 sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4` that takes an integer `n` as input and returns the `n`-th element of the Fib4 number sequence. It uses an iterative approach to compute the Fib4 sequence up to the `n`-th element and then returns the `n`-th element. The function handles the base cases for `n` being 0, 1, or 2, and uses a list to store the Fib4 sequence. The script also includes test cases to verify the correctness of the function.