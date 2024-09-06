```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a list containing a variety of values
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)  # Output: [2, 3, 3, 9, 123, 1]

# Test the function with a list of negative values
negative_list = [-1, -2, -3, -4, -5, -6]
result_negative = get_positive(negative_list)
print(result_negative)  # Output: []
```

This Python script defines a function `get_positive` that takes a list (`l`) as input and returns a new list containing only the positive numbers from the original list. It then applies this to test the function using a couple of test lists: