```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1, since we want a number smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```