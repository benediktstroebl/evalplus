```python
def median(l: list):
    """Return median of elements in the list l."""
    try:
        return (len(l) + 1) / 2 * float(sorted(l)[1])
    except IndexError:
        raise ValueError("The list must be sorted")
```