```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
        >>> largest_divisor(20)
        10
    """
    # Check if the input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    # Handle edge cases where n is less than or equal to 1
    if n <= 1:
        return 1

    # Start checking from n-1, as the problem statement asks for a divisor smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as it's the largest divisor smaller than n
            return i

    # This line should not be reached, as we've checked all possible divisors
    raise ValueError("No divisor found.")

# Test the function
print(largest_divisor(15))  # Should print: 5
print(largest_divisor(17))  # Should print: 1
print(largest_divisor(20))  # Should print: 10
```