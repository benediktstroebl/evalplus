```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
# Positive numbers: [2, 5, 6]
# Negative numbers: [-1, -4, 5]
# Complex numbers: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Test with different data types
names = ["Bob", "Alice"]
ages = [42, -1]
scores = [96, -80]

test_result = get_positive(ages)
assert len(test_result) == 2
test_result = get_positive([-1, 2, -4, 5])
assert len(test_result) == 4
test_result = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123])
assert len(test_result) == 9
test_result = get_positive(scores)
assert len(test_result) == 3
```