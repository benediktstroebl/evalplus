```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '']]

# Tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, '123']) == [0, 2, 3, 5, 9, '123']
```
This code defines a function called unique that takes a list as an argument and returns a new list containing only the unique elements from the original list. The function uses a way to generate the new list: it creates a set called seen to keep track of elements we have encountered so far. Then, it iterates through the elements of the input list and checks if the element is in the seen set. If it's not, it is added to the result list.