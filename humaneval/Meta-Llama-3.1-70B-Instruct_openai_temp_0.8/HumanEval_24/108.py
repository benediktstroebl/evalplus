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
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

    # If no divisor is found (should not happen for n > 1), return 1
    return 1


# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(30))  # Expected output: 15
print(largest_divisor(7))   # Expected output: 1

# Error test case
try:
    print(largest_divisor(-1))
except ValueError as e:
    print(e)  # Expected output: n must be a positive integer
```