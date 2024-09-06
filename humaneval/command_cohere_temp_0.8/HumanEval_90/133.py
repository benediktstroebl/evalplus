```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` utilizes the Python built-in sorting mechanism, `sort()`, to arrange the elements of the input list in ascending order. By doing this, the smallest element will be at the beginning of the list, followed by the second smallest element, and so on. The function then verifies if the length of the list is less than 2. If so, this implies that the list has only one or zero distinct elements, and in such cases, there is no second smallest element; hence, the function returns `None`. On the other hand, if there is a second element in the list, the function effectively returns the second smallest element, which is `lst[1]`. 

This approach does not require any additional importing of modules and is a straightforward way to solve the problem.