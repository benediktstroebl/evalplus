```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `set` function to remove duplicate elements from both lists and uses the `intersection` method to find the common elements between the two sets. The returned result is then sorted using the `sorted` function.

Here is an example usage of the above function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

The above examples are taken from the original problem statement and prove that the current solution passes the tests.