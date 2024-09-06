```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It uses the `set` function to remove duplicate elements and retrieves the unique elements that are present in both lists using the `intersection` method. These unique elements are then sorted using the `sorted` function and returned.

This solution is efficient with time complexity of O(M*N) where M and N are lengths of l1 and l2 respectively and efficient in space taking up O(N) memory. It is also deterministic, predictable, and does not contain any side effects as it provides the same output for the given input and does not change anything outside its scope.