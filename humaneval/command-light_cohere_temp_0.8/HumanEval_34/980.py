```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float()]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
try:
    [1, 2, 3, 4, 5, 6].unique()
except TypeError:
    assert False, "Should not raise error"

# Test case 3
class Test:
    def test_unique(self):
        return unique([])
test = Test()
assert test.unique()
```