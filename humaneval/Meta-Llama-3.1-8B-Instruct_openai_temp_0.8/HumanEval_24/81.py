### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    # If no divisors are found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```
This Python script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a loop to iterate from `n-1` down to `1` and checks if each number is a divisor of `n` by using the modulus operator (`%`). If a divisor is found, it is returned immediately. If no divisors are found, the function returns `1`, which is the only number that divides every integer evenly.