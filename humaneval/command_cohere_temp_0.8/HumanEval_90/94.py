```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```

The function `next_smallest()` uses the Python built-in sorted() function to sort the input list regardless of list size. Then, it checks if the length of the list is less than 2. If the list is empty or has only one element, it returns None, adhering to the prompt's specified return values for edge cases. If there are two or more elements, it returns the second element (index 1) after sorting, as this is guaranteed to be the second smallest value, matching the specification.