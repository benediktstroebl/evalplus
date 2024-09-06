```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

test_str = "abc123#$@%"
assert unique(test_str.match(re.maketrans()) == ["abc123", "#$@%"
```