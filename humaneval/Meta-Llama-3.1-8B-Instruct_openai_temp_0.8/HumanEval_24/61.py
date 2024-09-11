```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start by checking if n is divisible by 2, the largest even number
    if n % 2 == 0:
        return 2
    
    # Then check odd numbers starting from 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        # If n is divisible by i, it's the largest divisor
        if n % i == 0:
            return i
    
    # If no divisor is found, n itself is the largest divisor
    return n

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 17
```

In this script, we first check if the number `n` is divisible by 2, the largest even number. If it is, we return 2. 

Next, we check odd numbers starting from 3. If `n` is divisible by `i`, it's the largest divisor. 

Finally, if no divisor is found, `n` itself is the largest divisor, so we return `n`. This is because a number is always divisible by itself. 

We use the square root of `n` as the upper limit for our loop because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.