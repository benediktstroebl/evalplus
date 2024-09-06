```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are present in both lists. This is done using the `set` data type in Python, which automatically removes duplicate elements. The `intersection` method returns a set of the elements that are present in both `l1` and `l2`. Finally, the result is sorted to ensure that the elements are ordered numerically. 

This solution corresponds to the test cases mentioned in the problem statement. Let's verify the function behavior by testing it:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```
As expected, the function output is the same as in the initial description, confirming that the new solution behaves correctly.