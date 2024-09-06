```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
```
This function takes a list l as input and returns the median of its elements. It uses the method for the calculated median of an even number of data. In the first case, the median is calculated by adding the middle two elements and dividing by 2. In the second case, the median is simply the middle element.