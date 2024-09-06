```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are common in both lists. This is done using the `set` data type in Python, which removes duplicate elements by design. The `intersection` method is then used to find the common elements between the two lists, and `sorted` is used to ensure that the unique common elements are returned in order. 

This solution is efficient with time and memory complexity of O(m + n) where m and n are the lengths of l1 and l2 respectively. This is because the `set` data type in Python automatically removes duplicates, providing the method with a set of distinct elements from which to compute the intersection, and the `sort` method runs in linear time.