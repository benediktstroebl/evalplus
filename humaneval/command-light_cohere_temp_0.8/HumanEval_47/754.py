```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is != []), assert(len(l) > 1), "Input list must have more than one element")
    assert(all(type(x) == int for x in l)), "Input list must only contain integers"
    return (len(l) % 2 == 0) and (
        l[int((len(l) - 1) / 2)] +
        l[int((len(l) - 1) / 2) - 1]) / 2 or
        l[(len(l) - 1) / 2]
```