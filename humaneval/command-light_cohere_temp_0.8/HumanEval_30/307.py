```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with different input
test_data = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

# Test the function on the test_data
print(f"The list with only positive numbers: {get_positive(test_data)}")
```