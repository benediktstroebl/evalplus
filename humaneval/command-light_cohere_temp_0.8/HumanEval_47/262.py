```python
def median(lst):
    # Sort the list
    lst.sort()
    return (len(lst), list(sorted(lst)))[1] / 2
```