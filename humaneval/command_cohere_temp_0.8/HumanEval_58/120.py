```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and removes elements that are not present in both lists using the `intersection` method. Lastly, the returned unique common elements are sorted using the `sorted` function. 

This solution is concise and efficient, capable of handling various scenarios, and ensures the returned list is always sorted. You can verify the function's behavior and edge-case handling through testing, for example:
```python
# Test case for common function
def test_common():
    # Test case 1
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case 2
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test case 3
    assert common([], [1, 2, 3]) == []

    # Test case 4
    assert common([1, 2, 3], []) == []

    # Test case 5
    assert common([1, 2, 3, 4, 5], [3, 5, 7, 8, 9]) == [3, 5]

test_common()
``` 
This test suite covers multiple scenarios, including empty lists, different list lengths, and varying elements.