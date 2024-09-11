```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Raises:
        ValueError: If n is less than or equal to 1.
    """
    if n <= 1:
        raise ValueError("Input number must be greater than 1")

    # Start from n-1 and decrement by 1 until we find a divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can use a more efficient approach by only iterating up to the square root of n:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Raises:
        ValueError: If n is less than or equal to 1.
    """
    if n <= 1:
        raise ValueError("Input number must be greater than 1")

    # Start from sqrt(n) and decrement by 1 until we find a divisor
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Return the larger divisor
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
```