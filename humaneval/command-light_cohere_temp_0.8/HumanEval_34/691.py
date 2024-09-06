```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This Python code defines a function unique that sorts and returns unique elements from an input list. It uses a easydictation to keep track of unique elements in the seen set and returns a new list with those elements. The test_unique function tests the test_unique, which creates a list with a mix of numbers and texts and then asserts that unique correctly identifies the unique elements from the input list.