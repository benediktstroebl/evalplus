```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]  # return list with elements from l and 1 as additional element

# Test cases
test_incr_list = []
test_incr_list.append([5, [1, 2, 3])
test_incr_list.append([5, [2, 3, 4])
test_incr_list.append([5, [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
test_incr_list.append([5, [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])

# Function test
def test_incr_list():
    for test_case in test_incr_list:
        assert incr_list(test_case) == test_case

test_incr_list()
```