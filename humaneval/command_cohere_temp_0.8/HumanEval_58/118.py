```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the common elements between the two sets. The result is then sorted using the `sorted` function to ensure a consistent order for the output. 

This solution is efficient under the assumption that the two lists are not excessively large, where the complexity is governed by the logarithmic time required to remove duplicates and find the intersection. 

To better understand the solution a sample output is provided below:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```