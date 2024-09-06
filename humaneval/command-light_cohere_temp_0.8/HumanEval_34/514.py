```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -DELTA_INF]]

# Test 1: Verify correct behavior for negative values
assert len(unique([5, 3, 5, 2, 3, 3, -123] )) ==  6
# Test 2: Verify correct behavior for repeated values
assert len(unique([5, 3, 5, 3, 3, 9, 0, 123])) ==  6
```
The function unique returns a list with unique elements (not including None or negative infinity) from the input list. This is can also be useful for a variety of situations where you need to handle duplicate values in a list, such as removing duplicates from a set of items to be returned. The unique function is self-contained and may be used in a variety of contexts without the requirement of a list.