```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    n = len(l)

    # If the list has an even number of elements, return the average of the two middle numbers.
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    # If the list has an odd number of elements, return the middle number.
    else:
        return l[n//2]
```