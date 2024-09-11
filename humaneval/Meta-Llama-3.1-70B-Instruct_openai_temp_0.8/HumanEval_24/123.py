```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number should be greater than or equal to 2")

    # Start checking from n-1, as n itself is not considered
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(30))  # Expected output: 15

# Error handling test
try:
    print(largest_divisor(1))
except ValueError as e:
    print(e)  # Expected output: Input number should be greater than or equal to 2
```