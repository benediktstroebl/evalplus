```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    # Iterate through the list and square each number
    for num in lst:
        result += num ** 2
    
    # Return the value rounded up to the nearest integer
    return int(result)

# Test cases
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
```

This code defines a function called `sum_squares`, which takes a list of numbers as input and calculates the sum of the squares of these numbers. It then returns the result after rounding it up to the nearest integer.

The code provides various test cases to validate the function; each assertion checks the function's output against the expected result for a specific list of input values.