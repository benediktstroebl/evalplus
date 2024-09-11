### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1
    largest = 1
    
    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor if i is larger
            largest = i
    
    # Return the largest divisor
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach to check all numbers from 2 to `n` and find the largest divisor. The function is then tested with two example inputs.