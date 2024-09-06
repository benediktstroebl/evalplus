```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to return the elements in a consistent order. As the original problem stipulates, the result is a list of these common elements. 

This solution is efficient with a time complexity of O(m + n) where m and n are the lengths of the two lists. This is due to the efficiency of the `set` function which runs in O(n) for lists of integers. 

This solution provides a clear and concise way to solve the problem without relying on any external libraries.