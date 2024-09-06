```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `set` function to remove duplicate elements from both lists and uses the `intersection` method to find the common elements between the two sets. The `sorted` function is then used to sort the result. 

This solution is efficient with time complexity of O(min(len(l1), len(l2))).

Here is an example usage of the above function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```