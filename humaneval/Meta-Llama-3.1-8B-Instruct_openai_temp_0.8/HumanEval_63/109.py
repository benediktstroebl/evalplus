```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position in the FibFib sequence to compute.

    Returns:
        int: The nth element of the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases for n <= 2
    if n <= 2:
        return 0 if n == 1 or n == 0 else 1

    # Initialize a list to store the computed Fibonacci numbers
    fibfib_numbers = [0, 0, 1] + [0]*(n-2)

    # Compute the Fibonacci numbers iteratively
    for i in range(3, n+1):
        fibfib_numbers[i-1] = fibfib_numbers[i-2] + fibfib_numbers[i-3] + fibfib_numbers[i-4]

    return fibfib_numbers[n-1]


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```