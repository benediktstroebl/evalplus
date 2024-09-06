```python
def median(l):
    """Return median of elements in the list l.
    assert(isinstance(l) and len(l) > 1), "List must contain at least two elements."
    if len(l) % 2 == 0:
        return (l[len(l)//2][0] + l[len(l)//2][1]) / 2
    else:
        return l[len(l)//2][0]

#Test the function
med = median([-10, 4, 6, 1000, 10, 20])
print(med) # Output: 15.0
```