```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test function
def test_incr_list():
    l = [1, 2, 3]
    result = incr_list(l)
    assert l == result
    assert len(result) == 6
    assert all(result[i] >= i for i, x in enumerate(l))

# Test case 2
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(l)
assert l == result
assert len(result) == 14
assert all(result[i] >= i for i, x in enumerate(l))

# Test case 3
def test_equality():
    assert incr_list([1, 2, 3]) == [1, 2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

test_incr_list()
test_equality()
``` 
This code defines the `incr_list` function, which simply appends 1 to each element of the input list, effectively incrementing its elements by 1. The test_incr_list function tests the correctness of the `incr_list` function by creating lists with known values and ensuring that the incremented list matches the expected result. 
The test_equality function further tests the `incr_list` function by comparing it with the original list and an expected result.