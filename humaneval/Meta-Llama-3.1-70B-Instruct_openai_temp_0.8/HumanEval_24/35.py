```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """

    # Start from n-1 and decrement by 1 in each iteration
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```

In this script, the `largest_divisor` function works by iterating over numbers from `n-1` down to `1` and checking if each number is a divisor of `n`. As soon as it finds a divisor, it returns that number, because it's the largest one due to the order of iteration.