```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the elements that are common in both lists. Finally, it uses the `sorted` function to return the common elements in sorted order.

Here is an example usage of the above function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

The above examples are similar to the ones provided in the problem statement, testing the function with two lists containing common and unique elements.