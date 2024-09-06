```python
def unique(lst):
    return list(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

#main code
test_unique()
```
This script defines a function called unique that takes a list as input and returns a new list with unique elements from the original input list, using the set() function to remove duplicates. It also has a unique() function some series of test cases, which verify that the unique() function works correctly.