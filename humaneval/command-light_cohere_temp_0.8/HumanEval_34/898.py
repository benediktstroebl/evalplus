```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not spot[]]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

```
This code provides a function named unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses a specific techniques, such as a set to keep track of seen elements and a generator expression to filter out duplicates from the list. The test_unique function tests the for the function and asserts that it produces the correct result.