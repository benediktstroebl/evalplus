```python
def median(l: list):
    """Return median of elements in the list l.
    return float(''.find_medians(l))
    return l[len(l)//2]

def find_medians(l: list):
    m = []
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            i += 2
        else:
            m.push(l[i])
            i += 1
    return m
```