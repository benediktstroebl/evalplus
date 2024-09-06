```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases using a markdown code block
```python
 - This is a test case with a list of values and the expected output:  [2, 5, 6]
 - Another test case with a mix of values, including negative ones: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
 ```python
 - Test case with a list generated dynamically: ([1, 2, 3, -9, 0])
 - Test case with a empty list: []

# expected output: []
```