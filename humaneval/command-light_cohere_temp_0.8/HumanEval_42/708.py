```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

#Test case 1
assertEqual([1, 2, 3], [2, 3, 4])

#Test case 2
assertEqual([5, 3, 5], [6, 4, 6])

#Test case 3
assertEqual([5, 3, 5, 2, 3, 3], [5, 4, 6, 3, 4, 4])

#Test case 4
assertEqual([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
```