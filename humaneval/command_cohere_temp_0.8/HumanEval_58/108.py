```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two resulting sets. Finally, these common elements are sorted using the `sorted` function. 

This solution is efficient with time and space complexity of O(m*n) where m and n are lengths of l1 and l2 respectively. This is due to the efficiency of the `set` function which runs in O(n) and `intersection` which runs in O(m*n). The `sorted` function is O(n log n) but as it's only acting on a small subset of elements, the overall complexity is dominated by the `set` and `intersection` operations.