```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    >>> largest_divisor(15)
    5
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from the largest possible divisor (n // 2)
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(31))  # Output: 1
```