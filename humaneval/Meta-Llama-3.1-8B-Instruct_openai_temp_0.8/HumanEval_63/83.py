### FibFib Number Sequence
#### Efficient Computation of the n-th Element

We can use dynamic programming to efficiently compute the n-th element of the FibFib number sequence. Here's a Python script that implements this approach:

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    defined as follows:
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
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the computed elements
        fibfib_sequence = [0, 0, 1] + [0]*(n-2)

        # Compute the elements of the sequence
        for i in range(3, n+1):
            fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]

        return fibfib_sequence[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a list to store the computed elements of the FibFib sequence, which allows it to efficiently compute the n-th element in O(n) time. The function first checks the base cases, and then uses a loop to compute the elements of the sequence. It finally returns the n-th element of the sequence.