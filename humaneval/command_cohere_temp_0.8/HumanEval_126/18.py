```python
def is_sorted(lst):
    # Count the unique elements and sort the list if it's length is greater than 1
    if len(set(lst)) > 1: 
        lst.sort()
    # Check if the list is unchanged after sorting
    return lst == list(range(min(lst), max(lst) + 1, 1))
```