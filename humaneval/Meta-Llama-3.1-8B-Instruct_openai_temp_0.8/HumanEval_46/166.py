**Fib4 Number Sequence**
========================

Below is a Python script that efficiently computes the n-th element of the Fib4 number sequence using dynamic programming.

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Parameters
    ----------
    n : int
        The index of the Fib4 number to be computed.
        
    Returns
    -------
    int
        The n-th element of the Fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the computed Fib4 numbers
    fib4_numbers = [0] * (n + 1)
    fib4_numbers[2] = 2
    fib4_numbers[3] = 0
    
    # Compute the Fib4 numbers from index 4 to n
    for i in range(4, n + 1):
        # Calculate the next Fib4 number as the sum of the previous four numbers
        fib4_numbers[i] = fib4_numbers[i - 1] + fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4]
    
    # Return the computed n-th Fib4 number
    return fib4_numbers[n]

# Test the function with the provided examples
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence by storing the previously computed numbers in a list. This approach avoids the overhead of recursive function calls and reduces the time complexity of the algorithm.