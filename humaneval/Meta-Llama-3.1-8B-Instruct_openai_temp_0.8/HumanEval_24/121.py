```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): A positive integer
    
    Returns:
        int: The largest divisor of n smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 20
print(largest_divisor(17))  # Expected output: 17
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1`, checking each number to see if it is a divisor of `n` by using the modulus operator (`n % i == 0`). As soon as it finds such a number, it returns it. If no such number is found, the function will not return anything meaningful (since it will have reached `i=0` without finding a divisor). In practice, this will only happen if `n` is 1.

Note that this function is not very efficient for large inputs because it has to check every number less than `n`. A more efficient solution would involve finding the largest prime factor of `n` and then dividing `n` by that prime factor to get the largest divisor.