```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")

    # Start from the largest possible divisor and go down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Example use case
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can also solve this problem with a more mathematical approach, finding the largest factor directly:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")

    # For even numbers, the largest divisor is n // 2
    if n % 2 == 0:
        return n // 2
    # For odd numbers, the largest divisor is n // 3 or less, but not less than sqrt(n)
    else:
        for i in range((n // 3) + 1, int(n ** 0.5) - 1, -1):
            if n % i == 0:
                return i
        # If no other divisor is found, n is a prime number squared, return the square root
        return int(n ** 0.5)

# Example use case
print(largest_divisor(15))  # Output: 5
```