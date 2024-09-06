```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.push_into_list([[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]])

# Function Test Execution
results = get_positive(test_get_positive)

# Test Evaluation
assert all(results == [[-4, 2, 5, 6, -3, 3, 9, 123]))
```