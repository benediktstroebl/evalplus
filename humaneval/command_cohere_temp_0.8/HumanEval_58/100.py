```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is used to ensure that the resulting common elements are returned in a sorted manner. The code is encapsulated in a test block that checks correctness with the provided test cases. 
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

This will help ensure that the function behaves as expected and produces the correct results for various input scenarios.