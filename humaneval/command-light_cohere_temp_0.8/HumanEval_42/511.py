```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Simple increment
test_case1 = [1, 2, 3]
result1 = incr_list(test_case1)
assert result1 == [2, 3, 4]

# Test case 2: Recursion and different starting value
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result2 = incr_list(test_case2)
assert result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3: Complex list with different increment value
test_case3 = [1, 2, 3, 4, 5, 6, 7, 8]
result3 = incr_list(test_case3)
assert result3 == [2, 3, 5, 6, 7, 8]

print("All tests passed!")
```