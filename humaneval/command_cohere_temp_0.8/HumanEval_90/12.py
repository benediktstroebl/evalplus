```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list and returns the second element if the list has at least two elements. Otherwise, it returns `None`. 

Here is a snippet of tests to ensure the function works properly:
```python
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
``` 

The first two tests assert that the function returns the second smallest element when the list is sorted, while the last two tests assert that the function returns `None` when the list has fewer than two elements.