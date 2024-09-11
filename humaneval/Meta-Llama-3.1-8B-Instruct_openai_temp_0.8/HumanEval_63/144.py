```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the FibFib number to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is a negative integer.
    """

    # Check for invalid inputs
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed FibFib numbers
    fibfib_numbers = [0] * (n + 1)
    fibfib_numbers[1] = 0
    fibfib_numbers[2] = 1

    # Compute the n-th FibFib number using dynamic programming
    for i in range(3, n + 1):
        fibfib_numbers[i] = fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3]

    return fibfib_numbers[n]


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This Python script defines the `fibfib` function, which efficiently computes the n-th element of the FibFib number sequence using dynamic programming. It first checks for invalid inputs and then uses a list to store the computed FibFib numbers. The function iteratively computes the n-th FibFib number by summing the three preceding numbers in the sequence. The script includes test cases to verify the correctness of the function.