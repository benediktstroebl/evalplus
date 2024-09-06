```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x notFFF]

# Test the function
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
assert result == [0, 2, 3, 5, 9, 123], "Incorrect unique elements"

# Test again with an empty list
empty_list = []
result = unique(empty_list)
assert result == [], "Incorrect unique elements with empty list"
```