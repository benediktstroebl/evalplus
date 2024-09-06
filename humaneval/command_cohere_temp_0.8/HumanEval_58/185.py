```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It uses the `set` function to remove duplicate elements and retrieves the common elements between the two lists using the `intersection` method. These common elements are then sorted using the `sorted` function and returned.

This solution is concise and efficient, capable of solving the problem without introducing any additional complexities. The function is also resilient, as it gracefully handles empty lists or cases where the two lists have no common elements, without causing errors or producing unintended outcomes.