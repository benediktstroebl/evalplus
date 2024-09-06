```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It utilizes the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the elements that appear in both lists. To ensure that the output is sorted, the `sorted` function is applied to the result. 

This solution is efficient with a time complexity of O(m + n) where `m` and `n` are the lengths of `l1` and `l2`, respectively. This is because the algorithm executes the `set` and `intersection` operations, which each take O(n) time, and the `sorted` operation which takes O(m + n) time.