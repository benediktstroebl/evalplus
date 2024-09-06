```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This solution is efficient and has a time complexity of `O(min(len(l1), len(l2)))`. It is also scalable, adaptable, and minimizes the number of operations with the use of optimized Python collections.