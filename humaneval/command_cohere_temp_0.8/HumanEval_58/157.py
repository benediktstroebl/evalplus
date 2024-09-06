```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters. It uses the `set` function to remove duplicate elements from both lists and uses the `intersection` method to find the elements that are common in both lists. Then, to ensure that the output is sorted, it uses the `sorted` function to return the combined results. 

This approach ensures that the returned list contains only unique, sorted elements common to both input lists.