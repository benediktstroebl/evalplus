```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test cases
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Loop through test cases
for test in test_get_positive:
    actual = get_positive(test)
    expected = [2, 5, 6]
    assert actual == expected, f"ERROR: {test} was not expected."

print("All tests passed!")
```