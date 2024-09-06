```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and inherits the characteristic of ordering elements from `intersection` which returns elements common in both lists. Finally, the resulting list is sorted in ascending order. 

This function meets the criteria of the problem statement as it returns a list of unique elements that are present in both lists, and sorts these common elements. 

Here is a test case to verify the function:
```python
def test_common():
    # Test case one
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case two
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test case three
    assert common([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 1, 2]) == [1, 2, 6]

    # Test case four
    assert common([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

test_common()
```
This would run the function's corresponding test cases and return the expected outputs. 
If there are any other questions or concerns about the code, feel free to let me know!