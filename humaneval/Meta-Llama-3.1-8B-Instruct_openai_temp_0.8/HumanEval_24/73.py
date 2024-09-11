```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i
    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```

However, a more efficient solution can be achieved using a while loop and decreasing the divisor by 1 until we find the largest divisor.

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1
    i = n - 1
    # Keep decreasing i until it's a divisor of n
    while i > 1 and n % i!= 0:
        i -= 1
    # At this point, i is the largest divisor of n
    return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```