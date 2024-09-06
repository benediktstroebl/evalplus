```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements from both lists and uses the `intersection` method to find the elements that appear in both lists. To ensure uniqueness and sorting, the `sorted` function is applied to the result. This approach guarantees the return of sorted unique common elements between the two lists, conforming to the specified problem.

This function effectively solves the challenge of finding common elements in two lists and offers a concise and efficient solution. The utilization of the `set` function for uniqueness and the `intersection` method for element matching creates a streamlined approach to handle this problem. The `sorted` function further ensures that the returned result is correctly ordered.