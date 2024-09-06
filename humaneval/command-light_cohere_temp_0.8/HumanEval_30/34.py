```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Unit tests
test_get_positive = []

# Sample list input
test_get_positive.push_list([-1, 2, -4, 5, 6])

test_get_positive.push_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Add test cases for empty list input and lists with only negative numbers
test_get_positive.append([[]])
test_get_positive.push_list([])
test_get_positive.push_list([-5, -9, -123])

# Execute test suite
import pytest
pytest.py.test. pytest_case(test_get_positive)
```