```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to return the elements in a consistent order. 

This solution is efficient with a time complexity of O(m + n) where m and n are the lengths of l1 and l2 respectively, since `set` and `intersection` operations take O(n) time and `sorted` takes O(m) time.