### Largest Divisor Function
#### Finds the largest number that divides `n` evenly, smaller than `n`

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

    # Initialize the largest divisor to 1, since 1 divides every number
    largest_divisor = 1
    
    # Iterate from 2 to n (exclusive) to check for divisors
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor and larger than the current largest divisor, update it
            largest_divisor = max(largest_divisor, i)
    
    # Return the largest divisor found
    return largest_divisor
```

### Example Usage
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(17))  # Output: 1 (17 is a prime number)
```