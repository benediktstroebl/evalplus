```python
def median(l: list):
    """Return median of elements in the list l.
    m = len(l) // 2
    return (l[m-1] + l[m]) / 2 if m == len(l) // 2 else l[m]

# Test cases
l = [-10, 4, 6, 1000, 10, 20]
assert median(l) == 15.0

# Test case with one element
l = [20]
assert median(l) == 20

# Test case with empty list
l = []
assert median(l) == ""

# Test case with list of strings
l = ["Hello", "World"]
assert median(l) == "World"
```