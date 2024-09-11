```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Initialize the largest divisor to 1
    largest = 1
    
    # We only need to check up to the square root of n, because a larger factor of n would be a multiple of a smaller factor that has already been checked
    for i in range(2, int(n**0.5) + 1):
        # If i is a divisor of n, it could be the largest divisor
        if n % i == 0:
            # Update the largest divisor if i is larger than the current largest divisor
            largest = max(largest, i, n // i)
    
    return largest

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(10))  # Should print 5
```

This script works by iterating over all possible divisors of `n`, starting from 2. It keeps track of the largest divisor it has seen so far, and returns this at the end. The loop only needs to go up to the square root of `n`, because a larger factor of `n` would be a multiple of a smaller factor that has already been checked. The `max` function is used to update the largest divisor if a larger one is found.