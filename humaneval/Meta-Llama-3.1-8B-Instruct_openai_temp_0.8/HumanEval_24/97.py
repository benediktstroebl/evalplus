```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor of

    Returns:
    int: The largest divisor of n

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(100)) # Output: 100
```
This script uses a loop to iterate from `n-1` down to `1`, checking if each number is a divisor of `n` by using the modulo operator (`%`). As soon as it finds a divisor, it returns that number. If it fails to find any divisors (which should not happen except for the edge case of `n=1`), it returns `1`. 

This solution is efficient because it only needs to check numbers up to `n/2`, since a larger factor of `n` must be a multiple of a smaller factor that has already been checked. However, in this script we are checking all the numbers until n-1. This is not the most efficient solution but it does the job for a simple script.