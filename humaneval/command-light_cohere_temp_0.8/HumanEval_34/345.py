```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 2
class TestIterator(unittest.TestCase.TestCase):
    def test(self):
    assert len(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) == 6

# Test 3
def test_unique():
    assert unique([]) == []
```
This code includes the unique function that takes a list lst as input and returns a list of unique elements from the input, along with extensive tests to validate the correctness of the function.