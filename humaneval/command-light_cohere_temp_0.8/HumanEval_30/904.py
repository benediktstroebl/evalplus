```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
test_get_positive = []
test_get_positive.py  = [ [
    [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [-100, 2, 100] ]

# Function tests
for test in test_get_positive:
    actual_result = get_positive(test)
    expected_result = [x for x in test if x >= 0]
    assert actual_result == expected_result
```