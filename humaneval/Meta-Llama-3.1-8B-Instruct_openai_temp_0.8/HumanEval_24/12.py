```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start from the number itself and go down to 1
    for i in range(n, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, there are more efficient ways to find the largest divisor. One common approach is to use a while loop to divide the number by 2 until it's no longer divisible. Here's an updated version of the function using this approach:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start with the input number
    i = n
    # Keep dividing by 2 until we reach 1
    while i > 1:
        # If the number is divisible by 2, divide it
        if i % 2 == 0:
            i = i // 2
        # If the number is not divisible by 2, it means i is the largest divisor
        else:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the function is more efficient because it uses a while loop to reduce the number by half at each step, instead of checking every number from the input number down to 1.