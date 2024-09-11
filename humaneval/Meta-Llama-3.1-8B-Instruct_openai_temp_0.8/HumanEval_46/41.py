### Fib4 Number Sequence Computation
#### Using Dynamic Programming

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Raises:
    ValueError: If n is less than 0.
    """

    if n < 0:
        raise ValueError("Input should be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the sequence elements
    fib4_sequence = [0, 0, 2, 0] + [0] * (n - 3)

    # Compute the sequence elements using dynamic programming
    for i in range(4, n + 1):
        fib4_sequence[i - 1] = fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n - 1]


# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script defines a function `fib4` to compute the n-th element of the Fib4 number sequence. It uses dynamic programming to store the computed elements in a list and avoid redundant calculations. The function also includes input validation to ensure that the input is a non-negative integer. The test cases at the end verify the correctness of the implementation.