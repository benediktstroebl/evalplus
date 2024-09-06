```python
def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2
    else:
        return sorted_list[length // 2]
```