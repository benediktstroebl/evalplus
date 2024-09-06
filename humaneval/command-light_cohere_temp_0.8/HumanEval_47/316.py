```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        n = len(lst)
        m = n//2
        if n % 2 == 0:
            return (lst[(m-1)//2 + m] + lst[m//2]) / 2
        else:
            return lst[m]
    except IndexError:
        return "Input list is empty."
```