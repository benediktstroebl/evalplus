```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    elif lst[-2] > lst[-1]:
        return lst[-2]
    else:
        return lst[-1]
```

This function relies on the fact that the list is sorted in ascending order. It checks if the length of the list is greater than 1 and if the second last element is greater than the last element, then it returns the second smallest element, which is the second last element. If not, it returns the last element, which is the smallest element. This assumes that the list is properly sorted, and the behavior is undefined for unsorted lists.