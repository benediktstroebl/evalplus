```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 1.
    """

    # Check if n is less than 1, raise an error if true
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    # Initialize the largest divisor to 1
    largest = 1

    # Iterate from 2 to n-1 (inclusive)
    for i in range(2, n):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, update the largest divisor
            largest = i

    # Return the largest divisor
    return largest

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from 2 to `n-1` and checks if each number divides `n` evenly. If it does, it updates the largest divisor. Finally, it returns the largest divisor.