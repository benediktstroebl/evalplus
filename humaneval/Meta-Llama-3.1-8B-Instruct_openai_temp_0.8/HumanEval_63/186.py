```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the FibFib number to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the computed FibFib numbers
    fibfib_numbers = [0, 0, 1] + [0]*(n-2)
    
    # Compute the FibFib numbers from 3 to n
    for i in range(3, n+1):
        fibfib_numbers[i-1] = fibfib_numbers[i-2] + fibfib_numbers[i-3] + fibfib_numbers[i-4]
    
    # Return the n-th FibFib number
    return fibfib_numbers[n-1]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script provides a recursive function to compute the n-th element of the FibFib sequence. It uses memoization by storing previously computed FibFib numbers in a list to avoid redundant computations. The time complexity is O(n), and the space complexity is O(n) due to the list used for memoization. This function handles base cases and edge cases and provides test cases for verification.