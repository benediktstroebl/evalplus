```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are present in both lists. This is done using the `set` data type in Python, which removes duplicate elements by design. The `intersection` method is then used to find the elements that are present in both sets. These unique elements are then sorted using the `sorted` function and returned. 

This solution is able to handle lists of varying lengths and elements as shown in the example tests provided. It is also scalable, efficiently solving the problem for larger lists as well.