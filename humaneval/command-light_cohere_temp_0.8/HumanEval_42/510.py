```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
test_incr_list = [[1, 2, 3]]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test case 2
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
test_incr_list = [10, 20]
result = incr_list(test_incr_list)
assert result == [11, 21]
``` 
This Python code defines a function `incr_list` that increments elements of a given list by 1. It then tests the