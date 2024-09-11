```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # Return None if no divisor is found

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(30))  # Output: 15
print(largest_divisor(7))   # Output: 1
```