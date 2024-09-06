```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]

# Test cases
test_incr_list = [
    ( [], () ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], () ),
    ( [1, 2, 3], [4] )
]

def test_function(test_case):
    l = test_case[0]
    expected = test_case[1]
    got = incr_list(l)
    assert expected == got

test_incr_list = test_expand(test_case)

def test_expand(test_cases):
    test_incr_list = iter(test_cases)
    yield test_incr_list.
```

This code defines a function `incr_list` that adds 1 to the end of a list, and tests it with a series of test cases.  The use of the function `test_expand` to iterate over the test cases and yield them.