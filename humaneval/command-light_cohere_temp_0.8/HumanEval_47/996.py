```python
def median(lst):
    # Sort the list
    sorted_lst = sorted(lst)
    # Check length of list is even or odd
    if len(sorted_lst) % 2 == 0:
        # Find middle element
        middle = (len(sorted_lst) / 2)
        return sorted_lst[middle]
    else:
        # Find middle two elements
        middle1 = sorted_lst[(len(sorted_lst) / 2) - 1]
        middle2 = sorted_lst[(len(sorted_lst) / 2)]
        return (middle1 + middle2) / 2
```