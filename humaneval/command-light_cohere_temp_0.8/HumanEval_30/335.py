```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite using pytest
pytest.comporteurtest.pytest.pytestCOM a family. test.get_positive()
 read_tests
# valid: [-1, 2, -4, 5, 6]
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
# invalid: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```