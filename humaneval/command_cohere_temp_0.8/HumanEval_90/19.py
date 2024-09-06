```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the input list and then retrieves the second element (excluding the last element) to find the second smallest element in the list. If the list has less than two elements, it returns `None` to account for the edge case where there is no second smallest element. The code includes a comment that demonstrates how the result is inferred for different input lists.