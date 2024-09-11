```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for

    Returns:
        int: The largest divisor of n
    """
    # Start from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(12))  # Should print 6
print(largest_divisor(25))  # Should print 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to 1, checking if each number is a divisor of `n` by using the modulo operator (`%`). As soon as it finds a divisor, it returns that number.

The script also includes some test cases to demonstrate the function's behavior.