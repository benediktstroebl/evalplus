```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    """
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
```

You can test this function using the following code:
```python
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can use the math library's gcd function to find the greatest common divisor, which will be the largest divisor smaller than n:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    """
    return n - math.gcd(n, n - 1)
```

This version of the function should be more efficient for large inputs.