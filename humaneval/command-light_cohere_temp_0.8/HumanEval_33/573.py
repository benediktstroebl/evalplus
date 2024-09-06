```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) // 3 if x.isint() else x))
def is_integer(x):
    return x >= 0 and x <= 999999
```