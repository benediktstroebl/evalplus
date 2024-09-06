```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]

# Tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```
This script defines a function unique that takes a list lst as input and returns a new list containing only the unique elements from lst. The function uses a method set() to create a set of unique elements from the list, and then iterates over the list, appending elements to the set if they are not already in it.

The tests function contains a single assert statement that checks the correctness of the unique function. The assert statement fails if the result of unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) is not equal to [0, 2, 3, 5, 9, 123].