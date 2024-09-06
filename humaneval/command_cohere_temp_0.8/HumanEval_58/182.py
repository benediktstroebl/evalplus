```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `intersection` method to find the unique elements that appear in both lists, by utilizing the `set` data type to first remove any duplicate elements within `l1`. The resulting intermitted elements are then sorted using the `sorted` function. 

This solution is concise and efficient, capable of solving the problem without the need for additional data structures.