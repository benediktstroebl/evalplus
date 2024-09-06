```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1: return None
    elif len(l) % 2 == 1:
        return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
```
The median is calculated for lists with odd or even length. For lists with an odd length, the median is calculated as the average of the two middle numbers.