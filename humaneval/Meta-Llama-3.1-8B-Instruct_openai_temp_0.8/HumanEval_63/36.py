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
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        # Create a list to store the previous three FibFib numbers
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            # Update the previous three numbers
            a, b, c = b, c, a + b + c
        return c

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses a loop to compute the n-th FibFib number in O(n) time complexity, with a space complexity of O(1) since it uses a constant amount of space to store the previous three numbers.