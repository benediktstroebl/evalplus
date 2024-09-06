```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        return (left + right) / 2
```