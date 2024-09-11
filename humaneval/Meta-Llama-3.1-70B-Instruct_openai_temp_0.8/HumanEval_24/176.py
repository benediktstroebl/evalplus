```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We start from the largest possible divisor, which is n-1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can also use a more mathematical approach to solve this problem:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We start from the square root of n, as any factor larger than that would have a corresponding factor smaller than the square root
    for i in range(int(n**0.5), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return the larger of i and n // i
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the function is more efficient for larger inputs, as it only checks up to the square root of `n`.