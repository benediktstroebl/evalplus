```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test suite
test_get_positive = [
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6], "Test 1 failed"
    )

test_get_positive2 = [
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1], "Test 2 failed"
    ]
```