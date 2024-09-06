```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements and utilizes the `intersection` method to find the elements that are common in both sets. To ensure these common elements are returned in sorted order, the function concludes by using the `sorted` function. 

This solution is concise and efficient, capable of solving the problem without the need for additional imports.