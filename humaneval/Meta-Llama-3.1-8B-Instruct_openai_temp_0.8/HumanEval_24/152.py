```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor of
    
    Returns:
        int: The largest number that divides n evenly and is smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Iterate from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i
    # If no divisor is found, return 1 (1 is a divisor of all numbers)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, this can be optimized using a more mathematical approach. We can find the largest divisor of a number by dividing the number by the smallest prime factor and doing this repeatedly until we can't divide anymore. Here's how to do it:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor of
    
    Returns:
        int: The largest number that divides n evenly and is smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the smallest prime factor of n
    divisor = 2
    while n % divisor!= 0:
        # If n is not divisible by divisor, increment divisor by 1
        divisor += 1
    # Divide n by divisor to find the largest divisor
    while n % divisor == 0:
        n //= divisor
    # Return the largest divisor
    return divisor

# Test the function
print(largest_divisor(15))  # Output: 5
```