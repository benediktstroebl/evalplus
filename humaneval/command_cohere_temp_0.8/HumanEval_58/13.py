```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique elements that are present in both lists. It uses the `set` data type to remove duplicate elements and then uses the `intersection` method to find the common elements between the two lists. Finally, the returned elements are sorted using the `sorted` function. The code is encapsulated in a self-contained function that can easily be reused in other projects. 

Here is an example of how to use the above function to verify the problem statement:
```python
def test_common():
    # Test Case 1
    l1 = [1, 4, 3, 34, 653, 2, 5]
    l2 = [5, 7, 1, 5, 9, 653, 121]
    assert common(l1, l2) == [1, 5, 653]

    # Test Case 2
    l1 = [5, 3, 2, 8]
    l2 = [3, 2]
    assert common(l1, l2) == [2, 3]

test_common()
```

The test code uses the `common` function to verify the given test cases, checking if the output of the function matches the expected result.