### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1
    largest = 1
    
    # Iterate from 2 to n-1 (inclusive) to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor if necessary
            largest = i
    
    return largest

# Example usage:
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iteration over the range from 2 to `n-1` to find the largest divisor. The example usage at the end demonstrates how to use the function.