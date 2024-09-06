```python
def median(l: list):
    """Return median of elements in the list l."""
    m = []
    for i in range(len(l)//2):
        m.append(l[i])
    return (m if len(m)==1 else median([m[0:len(m)-1]]))

def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 0, 2, 4]
    assert median(lst) == 5.0
```