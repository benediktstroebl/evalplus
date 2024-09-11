```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n
    """
    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

This script defines the `largest_divisor` function, which iterates over numbers from `n-1` down to `1`, checking each one to see if it divides `n` evenly (i.e., with a remainder of 0). As soon as it finds such a divisor, it returns that number as the largest divisor of `n`. The script then tests this function with the input `15` and prints the result.