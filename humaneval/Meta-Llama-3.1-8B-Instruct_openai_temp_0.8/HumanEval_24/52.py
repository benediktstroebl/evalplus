### Largest Divisor
#### Python Script

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Iterate from n down to 1 to find the largest divisor
    for i in range(n - 1, 0, -1):
        # Check if n is divisible by the current number
        if n % i == 0:
            # If n is divisible, return the current number as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from `n - 1` down to 1 and checks each number to see if it divides `n` evenly. If a divisor is found, it is returned immediately. The function is then tested with the example input `n = 15`, which results in the expected output `5`.