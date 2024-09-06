```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
        
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum formula for integers from 1 to n

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function definition takes an integer `n` as input and returns the sum of the first `n` integers, following the formula `n(n + 1) / 2`. The argument is passed through tests, ensuring that the function correctly computes the sum for various values of `n`.  The function includes a comment that explains the mathematical formula used, which is a recursive approach to generating the sum.  This approach is efficient and can easily be scaled for larger integer inputs `n`.