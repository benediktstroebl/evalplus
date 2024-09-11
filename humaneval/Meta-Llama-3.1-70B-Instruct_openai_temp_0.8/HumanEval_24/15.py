```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Check if the input number is less than 2, in which case the largest divisor will be 1.
    if n < 2:
        return 1
    
    # Initialize the largest divisor as 1.
    largest_div = 1
    
    # Iterate over all numbers from 2 to n-1.
    for i in range(2, n):
        # Check if the current number is a divisor of n.
        if n % i == 0:
            # If it is, update the largest divisor.
            largest_div = i
    
    # Return the largest divisor found.
    return largest_div

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```
Alternatively, here is an optimized version of the function:
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Check if the input number is less than 2, in which case the largest divisor will be 1.
    if n < 2:
        return 1
    
    # Iterate over all numbers from n-1 down to 2.
    for i in range(n-1, 1, -1):
        # Check if the current number is a divisor of n.
        if n % i == 0:
            # If it is, return it as the largest divisor.
            return i
    
    # If no divisors are found, return 1.
    return 1

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```
This version starts from `n-1` and goes down to `2`, so it will find the largest divisor in the first iteration if it exists, making it more efficient.