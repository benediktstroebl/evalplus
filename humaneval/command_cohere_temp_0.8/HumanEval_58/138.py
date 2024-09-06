```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and assigns it the intersection of the two lists using the `intersection` method. Lastly, the function applies the `sorted` function to ensure that the elements are returned in a sorted order. The resulting output is a list of unique elements that appear in both lists.