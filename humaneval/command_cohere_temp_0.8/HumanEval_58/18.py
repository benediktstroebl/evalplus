```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements present in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This approach ensures that each element is included in the output only once, and the output is sorted accordingly. Let's verify the results using the provided test cases:
```python
def test_common():
    # Test Case 1
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test Case 2
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test Case 3
    assert common([1, 2, 3, 4, 5], [5, 4, 3, 1, 2]) == [1, 2, 3, 4, 5]

    # Test Case 4
    assert common([], [1, 2, 3]) == []

test_common()
```

The tests should pass successfully, confirming that the new implementation accurately solves the problem.