```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `intersection` method to find the unique common elements between the two lists. The `set` function is used to remove any duplicate elements from the list `l1`, and the `sorted` function is applied to return the elements in a sorted order.

This solution is concise and straightforward, and it should efficiently handle various scenarios. However, it's worth noting that the original problem statement includes some test cases with edge scenarios that may be worth addressing additionally.