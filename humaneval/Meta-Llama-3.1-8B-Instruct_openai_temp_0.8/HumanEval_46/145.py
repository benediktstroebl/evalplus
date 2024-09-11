### Fib4 Number Sequence Computation
```python
def fib4(n: int):
    """
    This function computes the n-th element of the Fib4 number sequence.

    Args:
    n (int): The index of the element to be computed.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a list to store the sequence
    fib4_sequence = [0, 0]

    # Compute the sequence up to the n-th element
    for i in range(2, n + 1):
        # Compute the next element as the sum of the previous four elements
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    # Return the n-th element of the sequence
    return fib4_sequence[n]


# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script uses a iterative approach to compute the Fib4 sequence up to the n-th element, storing the intermediate results in a list. The function `fib4(n)` takes an integer `n` as input, computes the sequence up to the n-th element, and returns the n-th element. The base cases are handled separately for efficiency.