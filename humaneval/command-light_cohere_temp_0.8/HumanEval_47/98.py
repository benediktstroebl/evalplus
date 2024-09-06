```python
def median(lst):
    # Sort the list
    lst.sort()
    calculate_median(lst)

def calculate_median(lst):
    if len(lst) == 0:
        return None  # Handle empty list
    middle = len(lst) // 2
    left_value = lst[middle - 1]
    right_value = lst[middle]
    return (left_value + right_value) / 2
```
This script defines a function called **calculate_median** that takes a list as input and calculates and returns the median of its elements.  The approach is to sort the list, then select the middle element(s), and average them to get the median.

This is a self-contained solution that does not require any additional functions or external imports.