```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
        
    Returns:
        int: The sum of integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2  # Sum formula for integers from 1 to n (inclusive)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function definition and test suite meet the problem requirements and provide a self-contained solution in a single code block. 

If you would like to test further with a different range of numbers, the code is set up to easily modify the input and verify the output through the assert statements. Feel free to change the values or add additional tests according to your requirements!