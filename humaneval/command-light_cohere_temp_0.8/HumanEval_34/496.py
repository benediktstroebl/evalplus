```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]: [None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This code defines a function unique that takes a list lst as input and returns a list of unique elements from the list. The unique elements uses a process of creating a set seen and then checks each element of the list against the elements in the set, and if the element is not in the set, then adds it to the output list.