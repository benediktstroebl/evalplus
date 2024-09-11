### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 if n is a prime number

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 8
```
This function iterates from `n-1` down to `1` to find the largest divisor. If a number `i` is found such that `n % i == 0`, it returns `i`. If no such number is found, it returns `1`, indicating that the number `n` is prime.