```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    
    if length % 2 == 0:
        return (sorted_lst[(length // 2) - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[(length // 2)]

# Test cases
median([3, 1, 2, 4, 5]) # 3.0
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([1, 2, 4, 5, 6]) # 3.0
median([20, 40, 60, 20]) # 20.0
median([-100, 200, -15]) # 15.0
```