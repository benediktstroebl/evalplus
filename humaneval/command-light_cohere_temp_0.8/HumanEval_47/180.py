```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        m = len(lst) // 2
        if m == 1:
            return lst[0]
        elif m == 2:
            return (lst[m-1] + lst[m]) / 2
        else:
            return (l[m-1] + l[m]) / 2
    except IndexError:
        print("IndexError:", lst)
        return None
    except ValueError:
        print("ValueError:", lst)
        return None
```