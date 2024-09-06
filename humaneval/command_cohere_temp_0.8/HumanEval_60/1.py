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

This function definition and test suite meet the problem requirements and demonstrate the sum formula for the first n natural numbers. 

If you would like to implement this algorithm in other ways, I am happy to provide other suggestions to solve this problem.