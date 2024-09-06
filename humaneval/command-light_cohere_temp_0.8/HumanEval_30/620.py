```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test case 1
test_suite = [
    [(-1,), (-4,), (-3,), (-10,)],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1],
    [-10]
]

for test in test_suite:
    actual_output = get_positive(test)
    assert actual_output == test
```