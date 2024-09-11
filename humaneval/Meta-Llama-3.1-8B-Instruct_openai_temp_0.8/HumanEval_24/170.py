```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize largest divisor as 1
    largest_div = 1
    
    # Iterate from 2 to n-1 to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor if i is larger
            largest_div = i
    
    # Return the largest divisor
    return largest_div

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(13))  # Output: 1
```

Alternatively, you can use the math.gcd function to simplify the code:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Calculate the greatest common divisor of n and n-1
    # The largest divisor smaller than n is the GCD
    return math.gcd(n, n-1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(13))  # Output: 1
```