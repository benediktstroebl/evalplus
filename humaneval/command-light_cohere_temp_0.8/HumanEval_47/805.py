```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0
```
The function uses the property of the median that if the list has an even length, then the median is the average of the two middle numbers. If the list has an length of odd numbers, the median is the middle element of the list.