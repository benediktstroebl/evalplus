```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the second largest divisor (n-1)
    for i in range(n-1, 0, -1):
        # Check if the number is a divisor of n
        if n % i == 0:
            # If it is, return the number
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```
This script implements the `largest_divisor` function by checking all numbers below `n` to see if they are divisors. It starts from the second largest number (`n-1`) and goes down to 1. As soon as it finds a divisor, it returns the number. The function includes a docstring that explains its purpose, input, output, and provides example usage.