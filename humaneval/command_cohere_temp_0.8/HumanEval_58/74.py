```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicate elements from both lists. The `intersection` method is then used to find the common elements between the two sets, and the result is sorted using the `sorted` function.

Here is an example of how you can use the `common` function to test its functionality:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

This shows that the `common` function works correctly and returns the sorted unique common elements for the given test cases. 
If you have any more questions or further assistance needed, let me know!