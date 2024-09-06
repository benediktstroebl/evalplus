```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `intersection` method to find the unique elements that appear in both lists, by leveraging the fact that sets automatically remove duplicate elements. The `sorted` function is then applied to ensure that the resulting common elements are returned in a sorted order. 
This solution provides a clear and concise implementation following the instructions in the code block.

Here are some example outputs to validate the function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```