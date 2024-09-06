```python
def unique(l: list):
    seen = set()
    return [element for element in l if element not in seen and element not in [0]]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
``` 
This code defines a function unique which takes a list l as input and returns a new list containing only the unique elements from l. It uses a unique elements in the list, but sets seen to a set to keep track of unique elements. This ensures that duplicates are skipped.