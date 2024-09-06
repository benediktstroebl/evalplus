```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

test_string = "Hello World"
assert unique(test_string) == ["Hello"]

test_set = {5, 3, 3, 0}
assert unique(test_set) == [0]
```