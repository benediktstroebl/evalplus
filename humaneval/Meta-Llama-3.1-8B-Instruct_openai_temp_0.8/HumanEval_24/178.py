### Largest Divisor
#### Python Script
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(17))  # Output: 1
```
This script defines a function `largest_divisor` that finds the largest number that divides the input `n` evenly, smaller than `n`. The function iterates over the numbers from `n - 1` down to 1, checking if each number is a divisor of `n` by using the modulo operator (`%`). As soon as it finds a divisor, it returns that number. If no divisors are found, the function returns 1, which is the trivial case (every number is divisible by 1).