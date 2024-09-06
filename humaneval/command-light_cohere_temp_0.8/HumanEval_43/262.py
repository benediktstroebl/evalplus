```python
def pairs_sum_to_zero(lst):
    return any(x + y <= 0 for x, y in zip(lst, lst[1:]))

# Test
test_data = [1, 3, 5, 0]
test_result = pairs_sum_to_zero(test_data)
assert test_result == False

test_data = [1, 3, -2, 1]
test_result = pairs_sum_to_zero(test_data)
assert test_result == False

test_data = [1, 2, 3, 7]
test_result = pairs_sum_to_zero(test_data)
assert test_result == False

test_data = [2, 4, -5, 3, 5, 7]
test_result = pairs_sum_to_zero(test_data)
assert test_result == True
```