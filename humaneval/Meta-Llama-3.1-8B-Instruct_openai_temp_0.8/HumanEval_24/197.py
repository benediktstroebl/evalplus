```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from n-1 downwards
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it's a divisor, return it immediately
            return i
    # If no divisor is found, return 1 (1 is a divisor of all numbers)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns its largest divisor smaller than `n`. It iterates from `n-1` downwards and checks each number to see if it divides `n` evenly (i.e., if `n % i == 0`). As soon as it finds a divisor, it returns that number. If no divisor is found, it returns 1, since 1 is a divisor of all numbers. The script also includes some example use cases to demonstrate the function's behavior.