### Efficient FibFib Number Sequence Computation in Python
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The index of the element to compute in the FibFib sequence.

    Returns:
        int: The nth element of the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """

    # Base cases
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed elements
    fibfib_sequence = [0, 0, 1] + [0]*(n-2)

    # Compute the elements of the FibFib sequence iteratively
    for i in range(3, n+1):
        fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]

    # Return the nth element of the FibFib sequence
    return fibfib_sequence[n]

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This script defines a function `fibfib(n)` that efficiently computes the nth element of the FibFib number sequence. It uses an iterative approach to store the computed elements in a list, which reduces the time complexity to O(n). The function raises a `ValueError` if n is less than 0, as the sequence is not defined for negative indices. The example usage demonstrates the function's correctness with the provided test cases.