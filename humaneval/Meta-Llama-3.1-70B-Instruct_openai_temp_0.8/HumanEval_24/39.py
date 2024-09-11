```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    # Start from n - 1 and check each number to see if it divides n evenly
    for i in range(n - 1, 0, -1):
        # If i divides n evenly, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(30))  # Output: 15
print(largest_divisor(7))   # Output: 1
```