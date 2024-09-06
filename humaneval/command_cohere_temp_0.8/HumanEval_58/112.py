```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements common in both lists, then sorts the result using the `sorted` function, and returns it. As noted in the description, the resulting list of elements will be sorted but will not retain their original ordering from the input lists. 

To ensure that no elements are modified during the process, the function utilizes the `set` data type to create a new collection of unique elements, leaving the original lists unchanged.