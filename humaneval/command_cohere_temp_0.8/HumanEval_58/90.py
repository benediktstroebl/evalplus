```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `intersection` method to find the unique common elements between them. The `set` function is used to remove any duplicate elements from the list `l1`, and the `sorted` function is applied to return the elements in a sorted order.

You can use this function by passing two lists as arguments to test it. 
For example:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

This will return the list of unique and sorted common elements in the two lists. 
The tool automatically completes this code block with an appropriate test setup and corresponding test scenarios to ensure the function behaves as expected. You can use it directly to solve the given problem and further adjust it based on your needs. G