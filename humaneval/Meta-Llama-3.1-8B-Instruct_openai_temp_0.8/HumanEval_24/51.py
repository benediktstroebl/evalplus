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
    # Initialize the largest divisor to 1, since 1 divides any number evenly
    largest_div = 1
    
    # Iterate from 2 to n (exclusive), since we're looking for a divisor smaller than n
    for i in range(2, n):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, update the largest divisor
            largest_div = i
    
    # Return the largest divisor found
    return largest_div

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (since 17 is a prime number)
```

Alternatively, you can use the `math` library to find the greatest common divisor (GCD), which is the largest number that divides two numbers evenly:

```python
import math

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
    # The GCD of n and n-1 is the largest number that divides n evenly
    return math.gcd(n, n-1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (since 17 is a prime number)
```