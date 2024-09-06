```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    if len(lst) % 2 == 1:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
```
This function takes a list as an argument and uses a simple algorithm to calculate the median of its elements. It handles the necessary cases and ensures the list is not empty and has a valid median.