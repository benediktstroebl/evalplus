```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the desired element in the Fibonacci sequence.

    Returns:
        int: The nth element of the Fibonacci sequence.

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the first 5 elements of the sequence
        fib4_sequence = [0, 0, 2] + [0]*(n-2)
        
        # Compute the sequence using dynamic programming
        for i in range(4, n+1):
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        
        return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines a function `fib4(n)` that uses dynamic programming to efficiently compute the nth element of the Fib4 number sequence. The function first checks the base cases and then initializes a list to store the first 5 elements of the sequence. It then computes the rest of the sequence using a loop, and finally returns the nth element. The script also includes test cases to verify the correctness of the function.