```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` uses the built-in Python `sorted()` function to sort the given list. Then, it checks if the length of the list is less than 2 or not. If the length is less than 2, it returns `None`. If the length is 2 or more, it returns the second element of the sorted list, which is the second smallest element of the original list. This solution follows the requirements of the given problem statement and should produce the desired outputs.