```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function named unique, which takes a list lst as input and returns a new list containing only the elements that are not in the set seen. The seen set is used to keep track of elements that have been seen so far. The function then loops through each element in the list and checks if it is not in the seen set and not None. The test_unique function contains a assert statement that checks the correctness of the unique function by passing the test list and expecting the expected output.