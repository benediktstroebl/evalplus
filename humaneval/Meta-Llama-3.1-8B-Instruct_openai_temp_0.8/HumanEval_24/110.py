### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    Examples:
    >>> largest_divisor(15)
    5
    """

    # Start from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function starts from the largest possible divisor (`n // 2`) and checks each number down to 1 to see if it is a divisor of `n`. If a divisor is found, it is returned. If no divisors are found, the function returns 1.