```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
assertEqual(get_positive([1, 2, 3, 4, 5, 6, 7]), [])

# Example usage
result = get_positive([-33, 123, -10, -5, 102, -8])
print(result)
 ```

This script defines a function `get_positive` that filters out any negative numbers from an input list and returns the positive ones. The test cases validate the general behavior of the function, and the example usage demonstrates its application to a specific list of numbers.