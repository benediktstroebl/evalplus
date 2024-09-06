```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```

This function sorts the input list before calculating the median, which is the median calculation procedure for most lists. It checks if the list has an odd number of elements, in which case it returns the element at the middle index. If the list has an even number of elements, it calculates the median as the average of the two middle elements.