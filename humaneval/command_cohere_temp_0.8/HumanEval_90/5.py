```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list and retrieves the second smallest element, or returns `None` if the list has less than two elements. 

Here is a snippet of tests to ensure the function behaves correctly:
```python
test_list = [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([], None),
    ([1, 1], None),
]

for test in test_list:
    assert next_smallest(test[0]) == test[1]
```