```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    assert len(result) == n + 1, f"Result list has incorrect length: {len(result)}"
    return result

# Test case 1
test_1 = [1, 2, 3]
test_1_result = incr_list(test_1)
assert test_1_result == [2, 3, 4]

# Test case 2
test_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_2_result = incr_list(test_2)
assert test_2_result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
test_3 = [0, 2, 3, 4]
test_3_result = incr_list(test_3)
assert test_3_result == [1, 3, 4, 5]

print("All tests passed!")
```