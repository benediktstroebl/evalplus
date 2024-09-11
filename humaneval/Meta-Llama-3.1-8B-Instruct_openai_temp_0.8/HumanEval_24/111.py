```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Parameters:
    n (int): The number to find the largest divisor for
    
    Returns:
    int: The largest divisor of n smaller than n
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

In this script, we define the `largest_divisor` function that takes an integer `n` as input. It iterates over all numbers from `n-1` down to 1, checking if each number is a divisor of `n` by checking if `n` modulo that number is 0. The first such number it finds is the largest divisor smaller than `n`, which it returns.

This function has a time complexity of O(n), where n is the input number, as in the worst-case scenario it needs to check all numbers smaller than n. However, for large values of n, it may be more efficient to use a more advanced algorithm that finds the largest divisor in O(sqrt(n)) time complexity.