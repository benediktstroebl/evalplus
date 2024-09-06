```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test the function with sample inputs
def test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Another test to ensure empty list gets empty list back
test_empty = unique([])
assert test_empty == []
```
This code defines a function unique that returns a list of unique elements from a given list lst, using a set seen to keep track of elements encountered so far. The test function is then tested with sample inputs and the output is verified against the expected result.