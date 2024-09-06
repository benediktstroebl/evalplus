```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2`, as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, and the `set` function to remove any duplicate elements. Finally, it uses the `sorted` function to sort the result. 

This solution corresponds to the specification of the problem and should work correctly. You can use it with Python lists `l1` and `l2` to obtain the common elements between the two lists, sorted, and without duplicates.