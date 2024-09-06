```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must have at least two elements")
    
    m = l[len(l)//2]
    i = len(l)//2
    while i >= 0 and m == l[i]:
        i -= 1
    return m

# Unit tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

test_median()
```