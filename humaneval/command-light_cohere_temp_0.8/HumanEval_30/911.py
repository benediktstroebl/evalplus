```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test cases
test_get_positive = [
    ( [-1, 2, -4], [2, 5, 6] ),
    ( [5, 3, -5], [5, 3, 9] ),
    ( [123], []),
    ( [1, -10], [1] ),
]

for case, expected in test_get_positive:
    actual = get_positive(case)
    assert actual == expected, "Error in case: " case + " expected != actual"
```