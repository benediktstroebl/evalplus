```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This function sorts the input list and returns the second element (second smallest) if the list has at least two elements. If the list has only one element or is empty, it returns None. This approach ensures the function handles all the test cases provided.