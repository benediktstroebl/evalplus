```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with sample inputs
test_get_positive = []
test_get_positive.py  # [-1, 2, -4, 5, 6]
test_get_positive.py  += [[2, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

# Run the function on test inputs and compare the results
test_get_positive = get_positive(test_get_positive.py)
print(test_get_positive)

# Test with a list of strings (should return an empty list)
test_empty_list = []
test_empty_list += ["Hello"]
test_empty_list = get_positive(test_empty_list)
print(test_empty_list)
```