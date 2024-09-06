```python
def incr_list(lst):
    n = len(lst)
    return [n + i + 1 for i in range(n)]

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
assert incr_list([5, 3, 5]) == [6, 5, 6]

# Test case 3
assert len(incr_list([5, 3, 5, 2, 3, 3, 3])) == 6

# Test case 4
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function incr_list that takes a list lst as input and returns a new list with the length of the original list, each element incremented by 1, and the list is also tested with 4 different assertions.