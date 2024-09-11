```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    
    Examples:
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Check if input is a positive integer
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    # Calculate sum using the formula for the sum of an arithmetic series
    sum_of_numbers = n * (n + 1) // 2
    
    return sum_of_numbers

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series. It checks if the input is a positive integer and raises a `ValueError` if it's not. The function is then tested with the provided examples.