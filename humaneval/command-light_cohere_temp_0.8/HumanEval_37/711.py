```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

#Test case 1
[1, 2, 3] = sort_even([1, 2, 3])
assert [1, 2, 3] == [3, 2, 1]

#Test case 2
[5, 6, 3, 4] = sort_even([5, 6, 3, 4])
assert [3, 6, 5, 4] == [4, 5, 6, 3]

#Test case 3
# This list has more than one odd element, which should return the list as it is
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] = sort_even([1, 2, 3, 4, 5])
assert [1, 2, 3, 4, 5] == [4, 5, 1, 2, 3]
```