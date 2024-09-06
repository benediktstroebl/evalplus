```python
def sort_even(l: list):
    return l[:][::2] + [x + 2 for x in l[1::2]]

#Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]

#Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

#Test case 3
assert sort_even([10, 2, 4, 7]) == [2, 4, 7, 10]
```