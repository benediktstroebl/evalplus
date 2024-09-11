```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    # Iterate over numbers from n-1 down to 1
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is the largest divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

You can save this code in a Python file, e.g., `largest_divisor.py`, and run it using `python largest_divisor.py` in your terminal.

This code defines the function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. The function uses a simple iterative approach, starting from `n-1` and checking each number down to 1 to see if it divides `n` evenly. The first such number it finds is the largest divisor of `n` that is smaller than `n`, and it is immediately returned. The code also includes a docstring and a test case to demonstrate the function's usage.