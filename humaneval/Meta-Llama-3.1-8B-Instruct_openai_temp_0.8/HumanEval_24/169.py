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
    """
    # Initialize the largest divisor as 1 (any number is divisible by 1)
    largest_div = 1
    
    # Iterate from 2 to n-1 (since we are looking for divisors smaller than n)
    for i in range(2, n):
        # Check if i is a divisor of n (i.e., n % i == 0)
        if n % i == 0:
            # If i is a divisor, update the largest divisor if it's larger
            largest_div = max(largest_div, i)
    
    return largest_div

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```

However, this solution has a time complexity of O(n) which might not be efficient for large inputs. A more efficient solution would be to find the largest divisor by iterating from n-1 down to 2 and checking for divisibility.

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
    """
    # Iterate from n-1 down to 2
    for i in range(n-1, 1, -1):
        # Check if i is a divisor of n (i.e., n % i == 0)
        if n % i == 0:
            # If i is a divisor, return i as the largest divisor
            return i
    
    # If no divisors are found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```

This solution has a time complexity of O(sqrt(n)) which is more efficient for large inputs.