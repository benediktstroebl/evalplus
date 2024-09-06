```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("List is empty.")
    elif len(l) == 1:
        return l[0]
    else:
        return (l[(len(l) + 1) // 2] + l[(len(l) - 1) // 2]) / 2
```
This code defines a function called median that takes a list as an argument and returns the median of the elements in that list. It handles cases where theequally-sized lists and where the list is empty or has only one element, returning the element itself in such cases. It also handles the additionally by averaging the two middle elements when the list has an even number of elements.