```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_unique_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_set = set(test_unique_list)
test_unique = unique(test_unique_list)

assert test_unique == [0, 2, 3, 5, 9, 123]
assert len(test_set) == len(test_unique)
```