```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is applied to sort the resultant common elements. The `common` function returns these sorted unique common elements between the two input lists. 

This solution has a time complexity of `O(min(n,m))`, where `n` and `m` are the lengths of `l1` and `l2`, respectively. This is because the worst-case scenario is when iterating through the smallest list, as we need to check every element in that list against the elements of the larger list. 

The space complexity is `O(1)`, as the resultant common elements are stored in a set data structure, which uses constant space. This complexity does not change regardless of the size of the input lists.