```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements and uses the `intersection` method to find the elements that are common in both sets. The `sorted` function is finally used to sort the result. This solution is 2 operations efficient and is also scalable. 

Here is an example of how you can test this function:
```python
def test_common():
    # Test list equality
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test list inequality
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test single element lists
    assert common([1], [1]) == [1]
    assert common([1], [2]) == []

    # Test empty lists
    assert common([], []) == []
    assert common([1, 2, 3], []) == []
```

The `test_common` function provides a variety of test cases that cover different scenarios. It verifies that the `common` function behaves correctly with respect to list equality, list inequality, single element lists, and empty lists. These tests can be used to validate the functionality of the `common` function.