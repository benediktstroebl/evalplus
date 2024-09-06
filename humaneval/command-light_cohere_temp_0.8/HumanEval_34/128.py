Here is a self-contained Python function that solves the problem of returning unique elements from a list:
```python
def unique(lst):
    set(lst)
    return list(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
test_unique()
```

This function utilizes the set() function to create a unique set of the list's elements, and then returns a list of the distinct elements. The test case demonstrates the unique() function with an example list. The code is self-contained, has minimal complexity, and efficiently solves the problem of getting unique elements from a list.