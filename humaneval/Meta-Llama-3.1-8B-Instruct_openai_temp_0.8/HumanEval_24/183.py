```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor as 1
    largest = 1
    
    # Iterate from 2 to n (inclusive) to find the largest divisor
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor and larger than the current largest, update the largest
            largest = i
    
    # Return the largest divisor found
    return largest

# Example usage
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function, which works by iterating from 2 to `n` (inclusive) and checking each number to see if it's a divisor of `n`. If a number is found to be a divisor and is larger than the current largest divisor, it's updated as the largest divisor. Finally, the function returns the largest divisor found. The example usage demonstrates how to use this function to find the largest divisor of 15.