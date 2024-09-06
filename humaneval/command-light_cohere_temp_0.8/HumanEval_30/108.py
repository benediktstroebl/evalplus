```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.add([range(-2, 10))
test_get_positive.add([range(-5, 5))
test_get_positive.add([range(0, 100))

# Execute test cases
for test in test_get_positive:
    assert get_positive(test) == [num for num in test if num >= 0] == [test]
```