```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from n-1, since we are looking for the largest divisor
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(20))  # Should print 10
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It starts checking from `n-1` and moving downwards, and returns the first number that divides `n` evenly.

The function includes a docstring that explains its purpose, parameters, return value, and possible exceptions. The script also includes test cases to verify the function's correctness.