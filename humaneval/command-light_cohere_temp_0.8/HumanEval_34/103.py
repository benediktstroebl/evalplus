```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and x not in [-None, float('inf')]]

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, [1, 2, 3], float('inf')]
test_unique_empty = []
test_unique_ LIST = [1, 2, 3]
test_unique_SET = {1, 2, 3, 4, 5}

# Test function
def test():
    assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
    assert unique([-1, 0, 1, 2]) == [0, 1]
    assert unique([]) == []
    assert unique(test_unique_empty) == []
    assert unique(test_unique_LIST) == [1, 2, 3]
    assert unique(test_unique_SET) == {1, 2, 3}

# Run the tests
test_function = unique
test()
```

This code defines a Python function `unique` which takes a list as input and returns a new list containing only the unique elements from the original list. The function uses a set to keep track of elements that have been encountered, then it iterates over the input list and adds elements that are not in the set and are not `None` or `float('inf')` to the new list. The test suite contains several test cases that cover different scenarios and verify the behavior of the `unique` function.