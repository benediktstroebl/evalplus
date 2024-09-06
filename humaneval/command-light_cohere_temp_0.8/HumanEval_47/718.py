```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
```
This function takes a list l as input and returns the median of its elements. The median is the average of the two middle numbers if the list has an odd length and the average of the two middle numbers if the list has an even length.