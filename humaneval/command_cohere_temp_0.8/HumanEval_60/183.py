```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
        
    Returns:
        int: The sum of integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2  # Sum formula for pairs of integers from 1 to n

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function definition takes an integer `n` as input and returns the sum of the first `n` integers. The formula `(n * (n + 1)) / 2` is used to calculate the sum, which is the sum of the first `n` odd integers and the first `n` even integers. The function is tested with a few specific values for `n` to validate its behavior.