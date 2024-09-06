```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. The generator expression `[x for x in l if not (x in seen or seen.add(x))]` checks if an element `x` is already in the set before adding it via the OR condition `or seen.add(x)`. The resulting list of unique elements is then sorted to ensure consistent output order. 

The unit tests demonstrated in the problem statement can be implemented as follows:
```python
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([-10, -20, -30, -40, -50, -30, -40]) == [-10, -20, -30, -40, -50]
```

By asserting the expected output against the output of the `unique` function for a variety of test cases, we can ensure that the function operates correctly and conforms to the problem statement's requirements. 
To run the tests, you can call the `test_unique` function and assert the truth of the returned boolean values.