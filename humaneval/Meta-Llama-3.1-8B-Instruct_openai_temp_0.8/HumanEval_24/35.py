### Largest Divisor Function
#### Python Script
```python
def largest_divisor(n: int) -> int:
    """
    This function finds the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.
    """
    # Initialize the largest divisor as 1
    largest_div = 1
    
    # Iterate from 2 to n (exclusive) to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor if i is larger
            largest_div = i
    
    return largest_div

# Example usage:
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from 2 to `n` (exclusive) to find the largest divisor. The example usage demonstrates how to use the function to find the largest divisor of 15, which is 5.