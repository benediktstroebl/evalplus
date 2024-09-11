```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor as 1, since 1 divides any number
    largest_div = 1
    
    # Iterate from 2 to n (exclusive) to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor if it's larger
            largest_div = max(largest_div, i)
    
    return largest_div

# Test the function with some examples
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```

However, a more efficient way to solve this problem would be to directly find the largest divisor by using the square root of the number as the upper limit for the division. Here's an updated version of the function:

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor as 1, since 1 divides any number
    largest_div = 1
    
    # Iterate from 2 to the square root of n (inclusive) to find the largest divisor
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor if it's larger
            largest_div = max(largest_div, i, n // i)
    
    return largest_div

# Test the function with some examples
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```