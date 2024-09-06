```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Number of integers to sum.
        
    Returns:
        int: Sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function uses the sum formula for the first n natural numbers, which is given by `n * (n + 1) // 2`. This works because the sum of odd numbers results in n * (n + 1) and the sum of even numbers results in n * n, and dividing by 2 balances the fact that there are n + 1 total numbers. 

To verify that the function behaves as expected, we have added tests to demonstrate the function's behavior for a few different input values. 

These tests assert that the function returns the expected value for various inputs to ensure the function works as expected.