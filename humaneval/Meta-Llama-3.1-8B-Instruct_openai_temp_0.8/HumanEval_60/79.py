```python
def sum_to_n(n: int):
    """
    Sums numbers from 1 to n using the formula for arithmetic series.
    
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
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    # Using the formula for arithmetic series: n*(n+1)/2
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for arithmetic series, `n*(n+1)/2`, to calculate the sum. The function also includes input validation to ensure that `n` is a positive integer. The script includes test cases to demonstrate the function's behavior.