```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, by leveraging the appropriately named `set` data type to first remove duplicates from `l1`. The result is then sorted using the `sorted` function to ensure consistent ordering. 

This solution is efficient with a time complexity of O(m + n) where m and n represent the lengths of the two lists. This is because the intersection operation used in the solution uses a hash-based approach with O(1) performance, and the sorting operation also has a time complexity of O(n log n). 

This approach offers a concise way to find common elements in two lists while ensuring uniqueness and a consistent sorting order.  This function can be readily used to solve problems involving common elements in various collections. 

Here are some example outputs of the function:
```
common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]

common([5, 3, 2, 8], [3, 2])
[2, 3]
```