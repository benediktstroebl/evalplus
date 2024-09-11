```python
# sum_to_n.py
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The number up to which the sum is calculated.
    
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

# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines the `sum_to_n` function, which uses the formula for the sum of an arithmetic series to efficiently calculate the sum of numbers from 1 to n. The formula is `n * (n + 1) / 2`, which is derived from the formula for the sum of an arithmetic series: `S = n/2 * (a1 + an)`, where `S` is the sum, `n` is the number of terms, `a1` is the first term, and `an` is the last term. In this case, `a1 = 1` and `an = n`, so the formula simplifies to `n * (n + 1) / 2`. The function is then tested with the provided examples.