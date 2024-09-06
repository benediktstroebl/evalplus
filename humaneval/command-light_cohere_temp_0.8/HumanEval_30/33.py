```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    dict(zip(['list'], [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    ]))
]

# Function Test
def test_function():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test negative input
test_negative = [
    dict(zip(['list'], [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    ]))
]

# Function Test2
def test_function2():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Run tests
import pytest
pytest.test.py
```