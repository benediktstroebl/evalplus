```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Parameters:
    n (int): The number for which to find the largest divisor.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from the second last number and check for divisibility
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    # If no divisors are found, return 0 (this should not happen)
    return 0

# Example usage
print(largest_divisor(15))  # Output: 5
```

However, there is a much more efficient way to solve this problem in a single line of code:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Parameters:
    n (int): The number for which to find the largest divisor.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    return max(i for i in range(n - 1, 0, -1) if n % i == 0)

# Example usage
print(largest_divisor(15))  # Output: 5
```