```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is used to ensure that the elements are returned in a coherent order. 

This approach ensures the returned list contains only unique, common elements, and maintains a consistent order. Let's verify the results using the given test cases:
```python
def test_common():
    # First Test Case
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Second Test Case
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Edge Case
    assert common([], []) == []

    # Edge Case
    assert common([1], [1, 2, 3]) == [1]

    # Edge Case
    assert common([4, 5, 6], [7, 6, 5, 4]) == [4, 5, 6]

test_common()
```

The tests should pass successfully, confirming that the updated `common` function appropriately returns sorted, unique common elements.