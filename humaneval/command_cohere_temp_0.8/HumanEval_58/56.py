```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to return the elements in a consistent order. Such a solution adheres to the given problem description and passes the tests provided. 

Here is an example of how to use the above code:
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This will output:
```
[1, 5, 653]
[2, 3]
```

The first output returns the sorted unique common elements of the two lists, `[1, 5, 653]`, while the second output returns the sorted unique common elements of `[5, 3, 2, 8]` and `[3, 2]`, `[2, 3]`.