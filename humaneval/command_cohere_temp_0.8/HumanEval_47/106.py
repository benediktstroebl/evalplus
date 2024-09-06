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

This function sorts the input list before calculating the median, which is a more efficient approach compared to the naive approach of iterating through the entire list to find the median. Also, the median function handles both odd and even-length lists. For odd lengths, it returns the middle element, and for even lengths, it computes the average of the two middle elements.