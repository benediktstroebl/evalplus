```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor as 1
    largest_div = 1
    
    # Iterate from 2 to n-1 (inclusive) to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest_div = i
    
    # Return the largest divisor
    return largest_div

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, this script is not the most efficient solution because it checks every number up to n-1. A more efficient solution would be to check each number from n-1 down to 2:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if it is a divisor of n
    for i in range(n-1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return i
            return i
    
    # If no divisor is found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the script is more efficient because it stops checking as soon as it finds a divisor, rather than checking every number up to n-1.