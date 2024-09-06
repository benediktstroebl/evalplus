```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
actual = get_positive(test_list)
expected = [5, 3, 2, 3, 9, 123, 1]

# Print the results
print(f"Expected: {expected}")
print(f"Actual: {actual}")
```