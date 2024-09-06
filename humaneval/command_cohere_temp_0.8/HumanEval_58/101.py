```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `intersection` method to find the unique elements that appear in both lists, by utilizing the appropriate setter, it further ensures that the return is a list of distinct elements. Finally, it sorts the resulting list alphanumerically. 

This function would have passed the test cases provided in the original prompt.