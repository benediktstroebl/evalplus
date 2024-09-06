```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and the `intersection` method to find the elements that are common in both sets. Finally, it calls the `sorted` function to return the common elements in sorted order.

Here is an example usage of the above function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

The examples illustrate how the `common` function effectively identifies and returns the unique common elements in two lists, demonstrating its usefulness in handling such scenarios.  This solution is efficient with a time complexity of O(min(len(l1), len(l2))).