```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with various lists of numbers
tests = [
    [ [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 10, 100 ] ]
]

for test_list in tests:
    actual = get_positive(test_list)
    expected = [2, 5, 6, 9, 123, 1]
    print(f"Test {test_list}: Actual={actual}, Expected={expected}")
    assert actual == expected
```