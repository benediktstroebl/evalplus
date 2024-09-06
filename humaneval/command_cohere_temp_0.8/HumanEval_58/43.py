```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is applied to keep the elements in question in sorted order. 

This approach ensures that each element is unique, and the order is predetermined by the sorting procedure. Let's confirm this operation with tests:
```python
def test_common():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([1, 2, 4, 3, 4, 2, 1], [1, 2, 4, 3, 2, 1]) == [1, 2, 3, 4]

test_common()
```

The test cases validate the function with different inputs and assert that the output is correct. You can use this opportunity to verify the functionality of the function and check if the code aligns with the problem statement. Let me know if you need anything else!