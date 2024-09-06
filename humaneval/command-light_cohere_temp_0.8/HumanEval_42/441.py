```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]

#Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = incr_list(test_incr_list)
assert result1 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

#Test case 2
test_incr_list = [5, 3, 5, 2, 3, 3]
result2 = incr_list(test_incr_list)
assert result2 == [6, 4, 6, 3]

#Test case 3
test_incr_list = [5, 3, 0, 2, 3, 3]
result3 = incr_list(test_incr_list)
assert result3 == [6, 4, 6]

print("All tests passed!")
```