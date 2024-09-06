```python
def median(l: list):
    """Return median of elements in the list l."""
    l = list(map(float, l))  # Convert the list to float numbers
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return (l[mid] + l[mid - 1]) / 2.0
   
    maximum = max(l)
    if len(l) % 2 == 1:
        return l[mid]
```