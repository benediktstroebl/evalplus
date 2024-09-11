```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1, since every number is divisible by 1
    largest = 1
    
    # Check all numbers from 2 to n-1 to see if they are divisors of n
    for i in range(2, n):
        # If n is divisible by i, then i is a divisor of n, and we update the largest divisor
        if n % i == 0:
            largest = i
    
    return largest

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
```

However, a more efficient way to solve this problem would be to use a loop that starts from `n // 2` (integer division of `n` by 2) and goes down to 1, since a larger factor of `n` must be a multiple of a smaller factor that has already been checked.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1, since every number is divisible by 1
    largest = 1
    
    # Start from the largest possible divisor and go down to 1
    for i in range(n // 2, 0, -1):
        # If n is divisible by i, then i is a divisor of n, and we update the largest divisor
        if n % i == 0:
            largest = i
            break
    
    return largest

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
```