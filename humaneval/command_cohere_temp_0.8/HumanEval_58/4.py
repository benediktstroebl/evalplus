```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `intersection` method to find the unique common elements between the two lists. The result is then sorted using the `sorted` function and returned.

Here is an example usage of the function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
```

And another example:
```python
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

As demonstrated, the function can successfully process multiple input scenarios and produce the desired outcome of sorted unique common elements. 
If you have any more queries, please don't hesitate to ask!