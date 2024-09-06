```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, by utilizing the `set` data type to first remove any duplicate elements within the list `l1`. The `sorted` function is then applied to organize the results in ascending order. 

This solution is efficient with time complexity of O(min(len(l1), len(l2))). It utilizes the built-in Python methods for efficient set and list intersection, ensuring simplicity and optimized performance.