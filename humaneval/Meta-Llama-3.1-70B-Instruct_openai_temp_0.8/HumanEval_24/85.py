```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from the largest possible divisor, which is n-1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

    # If no divisors are found (which is not possible in theory), return None
    return None


# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(20))  # Expected output: 10
```