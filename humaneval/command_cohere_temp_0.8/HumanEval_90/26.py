```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` utilizes the Python built-in sorting mechanism, `sort()`, to arrange the elements of the input list in ascending order. By doing this, the smallest element will be at the start of the list, followed by the second smallest, and so on. Subsequently, the function verifies if the length of the list is less than 2. If this is the case, it returns `None` as there is no second smallest element available. On the other hand, if the list contains 2 or more elements, the function retrieves the second smallest element from the sorted list, providing the desired result. 

This approach ensures a straightforward and efficient solution to retrieve the second smallest element from a list of integers. 

You can verify the functionality of the script by conducting tests on the four input cases provided in the prompt.