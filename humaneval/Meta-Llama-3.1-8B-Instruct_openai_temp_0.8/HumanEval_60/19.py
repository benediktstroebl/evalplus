```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum. It must be a positive integer.
    
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
    
    # Calculate the sum using the formula for the sum of an arithmetic series
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula `n * (n + 1) / 2`, which is a more efficient approach than using a loop. It also includes input validation to ensure that `n` is a positive integer. The test cases at the end of the script demonstrate the function's behavior with different inputs.