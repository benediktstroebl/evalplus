```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if the number is a divisor of n
    for i in range(n-1, 0, -1):
        # Check if n is divisible by i
        if n % i == 0:
            # If n is divisible by i, return i as the largest divisor
            return i
    # If no divisor is found, return 1 as the largest divisor (by definition)
    return 1

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(20))  # Should print 20
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest divisor of `n` smaller than `n`. The function works by starting from `n-1` and checking each number to see if it divides `n` evenly. If it finds a divisor, it returns that number. If it doesn't find any divisors, it returns 1 (since 1 divides all numbers evenly). The script then tests the function with a few examples to demonstrate its behavior.