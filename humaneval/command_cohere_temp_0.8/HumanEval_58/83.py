```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicate elements from both lists. The `intersection` method is then used to find the common elements between the two lists, and the result is sorted using the `sorted` function.

Here is an example of how you can use the `common` function to solve the problem:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

This example uses the `common` function to return the sorted unique common elements for the given lists. The function is called with two lists, `[1, 4, 3, 34, 653, 2, 5]` and `[5, 7, 1, 5, 9, 653, 121]`, and the output is `[1, 5, 653]`. For the second example, the output is [2, 3]. These results are the same as those shown in the original problem statement.