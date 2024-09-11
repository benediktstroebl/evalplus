### Fibonacci-like Sequence - Fib4
Here's a Python script that uses dynamic programming to calculate the n-th element of the Fib4 number sequence:

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    :param n: The index of the Fib4 number to calculate.
    :return: The n-th element of the Fib4 number sequence.
    """
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the list to store the sequence
    fib4_sequence = [0, 0, 2, 0] + [0]*(n-3)
    
    # Calculate the sequence iteratively
    for i in range(4, n+1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a list to store the calculated sequence elements. It initializes the list with the base cases and then iteratively calculates the remaining sequence elements. This approach has a time complexity of O(n) and a space complexity of O(n).