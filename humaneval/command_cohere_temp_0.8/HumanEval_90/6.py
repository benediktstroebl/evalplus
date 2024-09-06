```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element, returning `None` if the list has less than two elements. This approach is efficient and scalable, ensuring the function can handle various input scenarios effectively.