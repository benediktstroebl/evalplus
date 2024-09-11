```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.
    """
    # Start from n-1 and iterate downwards
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` downwards, checking each number to see if it is a divisor of `n`. As soon as it finds a divisor, it returns that number.

Note that this function assumes that the input number `n` is a positive integer. If `n` is not a positive integer, the function may not work correctly. If you need to handle non-positive integers or non-integer inputs, you will need to modify the function accordingly.