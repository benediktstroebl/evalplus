```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number must be greater than or equal to 2")

    # Start checking from n-1 downwards
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

    # If no divisors are found (which should not happen for n >= 2)
    return None


# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(100))  # Expected output: 50
```

This script defines the function `largest_divisor` which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach, starting from `n-1` and checking each number to see if it is a divisor of `n`. The first divisor found is returned as the result.

The script also includes test cases to verify the function's correctness.