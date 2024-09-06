```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, by leveraging the fact that sets discard duplicate values. To ensure that the result is sorted, the function applies the `sorted` function upstream. This solves the given problem and should pass the provided tests.