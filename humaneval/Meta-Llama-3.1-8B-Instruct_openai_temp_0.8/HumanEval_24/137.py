```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number
    
    Returns:
    int: The largest divisor of n smaller than n
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check for divisibility
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that finds the largest number smaller than `n` that divides `n` evenly. It starts from `n-1` and checks each number in descending order to find the first divisor, which is the largest one smaller than `n`. The function returns this largest divisor. The script includes a docstring to describe the function and its behavior, as well as a test case to demonstrate how to use the function.