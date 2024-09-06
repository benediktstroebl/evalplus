```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1] 

# Test the function with known inputs
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)

assert test_incr_list == result

# Test the function again with a more complex list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123, [1, 2, 3, 4]]
result = incr_list(test_list)

assert result == test_list
```