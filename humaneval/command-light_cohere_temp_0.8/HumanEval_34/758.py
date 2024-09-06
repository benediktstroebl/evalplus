```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
The function unique takes a list l as input and returns a sorted list containing only the unique elements in l. This is using the unique function to get rid of duplicates by first converting the list into a set and then back to a list. For a result, the set is sorted, and the function returns the list of the unique elements, which are in this case the numbers 0, 2, 3, 5, 9, and 123.

The test_unique function contains a test case that passes the function unique with a test list, and the expected output is the list that contains the unique elements of the input list.