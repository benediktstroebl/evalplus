```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (assuming the list has at least two elements). This handles the "edge cases" as described in the comment by returning `None` when the list is empty or has only one element. Using Python's `sorted()` function simplifies the process, making the code more concise and efficient.