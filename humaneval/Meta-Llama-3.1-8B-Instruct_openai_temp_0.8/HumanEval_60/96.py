```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    return n * (n + 1) // 2


# Test cases
print(sum_to_n(30))  
print(sum_to_n(100))  
print(sum_to_n(5))  
print(sum_to_n(10))  
print(sum_to_n(1))  
```

This script uses the formula for the sum of an arithmetic series: `n * (n + 1) / 2` to calculate the sum, making it efficient for large values of `n`.