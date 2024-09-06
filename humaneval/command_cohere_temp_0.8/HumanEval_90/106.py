```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This function leverages Python's built-in `sort()` method to sort the list in ascending order. Subsequently, it verifies if the length of the list is less than 2, returning `None` to signify the absence of a 2nd smallest element. However, if there are at least two elements, it returns the second element from the sorted list.

Here is a more robust version that handles scenarios where the list might be populated with duplicate entries:
```python
def next_smallest(lst):
    def check_second_smallest(lst):
        lst.sort()
        if len(lst) < 2:
            return None
        else:
            return lst[1]

    if len(lst) < 1:
        return None
    if len(lst) == 1:
        return None if lst[0] == lst[0] else lst[0]
    return min(check_second_smallest(set(lst)), check_second_smallest(set(lst)[1:]))
```

This updated version employs two instances of the `check_second_smallest` function, the second being a slice of the set with the first element excluded. This ensures that if the list has duplicate entries, the function returns the smallest unique value, serving as the 2nd smallest element.