```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is used to ensure that the elements are returned in a sorted order. The code is encapsulated in a test block that verifies the function against sample inputs, returning relevant elements as expected.

```python
def test_common():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
```

The test code uses the `assert` statement to compare the output of the `common` function against the expected output. If the output of the function matches the expected output, the test passes; otherwise, it fails, ensuring the function works correctly.