```python
def unique(lst):
    """Sorts and returns unique elements from a list"""
    seen = {}
    return [x for x in set(lst) if x not in seen and x not None]

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

#Test case 2
test_case2 = [5, 3, 'abc', 5, 'abc', 0, 123]
assert unique(test_case2) == ['abc', 5, 0]

#Test case 3
test_case3 = [f(5), 3.14]
assert not unique(test_case3) # This will fail until we use set()
```