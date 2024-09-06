```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite
test_get_positive = []

# Generate test cases
test_cases = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Run the tests
for test_case in test_cases:
    assert get_positive(test_case) == [2, 5, 6, 3, 9, 123, 1]
```
This script defines a `get_positive` function, which takes a list as input and returns a new list containing only the positive elements from the original list. 

The function utilizes list comprehension to filter out the negative elements from the input list.