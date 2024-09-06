```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        return (lst[-1] + lst[0]) / 2
```