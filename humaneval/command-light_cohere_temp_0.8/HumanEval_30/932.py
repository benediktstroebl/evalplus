```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite using pytest
pytest.run('positive numbers')

# Example usage
l = [1, 2, -4, 5, 6]
print(get_positive(l))  # Output: [2, 5, 6]
```
This script defines a function `get_positive` that takes a list as an argument and returns a new list with only the positive elements from the original list. It uses list comprehension to filter out the positive elements from the input list, and then returns the resulting list.