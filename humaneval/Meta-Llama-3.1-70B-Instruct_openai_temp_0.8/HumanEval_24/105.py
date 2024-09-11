```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(25))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```

This script defines a function `largest_divisor` that finds the largest number that divides the input number `n` evenly, which is smaller than `n`. The function iterates from `n-1` down to 1 and returns the first number that divides `n` without leaving a remainder. If no such number is found (i.e., `n` is a prime number), the function returns 1. The script also includes some test cases to demonstrate the function's behavior.