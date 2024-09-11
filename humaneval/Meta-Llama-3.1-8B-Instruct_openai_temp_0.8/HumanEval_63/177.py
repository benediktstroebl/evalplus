```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.
    """
    if n <= 1:
        # Base case: if n is 0 or 1, return 0
        return 0
    elif n == 2:
        # Base case: if n is 2, return 1
        return 1
    elif n <= 3:
        # Base case: if n is between 2 and 3, return 1
        return 1
    else:
        # Initialize variables to store the previous three numbers
        a, b, c = 0, 0, 1
        # Compute the n-th number in the sequence
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that calculates the n-th element of the FibFib sequence. It uses a loop to compute the sequence iteratively, storing the previous three numbers in variables `a`, `b`, and `c`. The function handles base cases for `n` less than or equal to 1. The script also includes test cases to verify the correctness of the function.

**Note:** This script has a time complexity of O(n), where n is the index of the element in the sequence. The space complexity is O(1), as it only uses a constant amount of space to store the previous three numbers.