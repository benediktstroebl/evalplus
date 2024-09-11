```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n smaller than n.
    """
    # Start checking from n-1, since we want the largest divisor smaller than n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is the largest divisor of n smaller than n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Outputs: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach to find the largest divisor. It starts checking from `n-1` and decrements by 1 until it finds a number that divides `n` evenly. The function includes a docstring that provides a description of the function, its arguments, and its return value. The script also includes a test case to demonstrate the function's usage.