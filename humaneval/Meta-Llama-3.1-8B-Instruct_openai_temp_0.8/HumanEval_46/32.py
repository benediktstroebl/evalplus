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
    
    Args:
        n (int): The index of the Fibonacci number in the sequence to be computed.
    
    Returns:
        int: The nth number in the Fib4 sequence.
    """
    if n <= 3:
        # Base cases
        return [0, 0, 2, 0][n]
    
    # Initialize a list to store the first n+1 Fibonacci numbers
    fib4_list = [0, 0, 2, 0]
    
    # Compute the n-th Fibonacci number
    for i in range(4, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    
    # Return the n-th Fibonacci number
    return fib4_list[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the nth Fibonacci number in the Fib4 sequence. It initializes a list with the base cases and then iteratively computes the remaining numbers in the sequence using the given recurrence relation. The function returns the nth number in the sequence. The test cases are included at the end to verify the correctness of the function.