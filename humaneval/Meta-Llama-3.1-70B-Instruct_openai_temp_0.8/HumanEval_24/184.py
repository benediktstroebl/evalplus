```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(20)
        10
    """
    # Start from n-1, as the problem asks for a divisor smaller than n
    for i in range(n-1, 0, -1):
        # Use the modulus operator to check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a for loop to iterate from `n-1` down to 1, checking each number to see if it divides `n` evenly using the modulus operator. As soon as it finds a number that divides `n` evenly, it returns that number as the largest divisor.

Alternatively, you can solve this problem using a more mathematical approach by iterating from `n//2` down to 1, as any number larger than `n//2` cannot divide `n` evenly.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(20)
        10
    """
    # Start from n//2, as any number larger than n//2 cannot divide n evenly
    for i in range(n//2, 0, -1):
        # Use the modulus operator to check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```