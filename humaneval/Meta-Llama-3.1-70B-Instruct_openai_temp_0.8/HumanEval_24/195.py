```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> largest_divisor(15)
        5
    """
    if n < 1:
        raise ValueError("Input number should be greater than 0")
    
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to 1 and checking if each number is a divisor of `n`. As soon as it finds a divisor, it returns that number. The script also includes a docstring with documentation and an example usage.