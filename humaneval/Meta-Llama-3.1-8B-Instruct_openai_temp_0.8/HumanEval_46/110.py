### Fib4 Number Sequence Implementation in Python
```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Initialize a list to store the first 5 elements of the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the n-th element using an iterative approach
    for i in range(4, n + 1):
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    return fib4_sequence[n]


# Test the function with example inputs
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines a function `fib4` that computes the n-th element of the Fib4 number sequence using an iterative approach. The function first initializes a list to store the first 5 elements of the sequence and then uses a loop to compute the remaining elements up to the n-th element. The function returns the n-th element of the sequence.