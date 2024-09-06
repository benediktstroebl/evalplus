```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==6 or raise ValueError("List must have exactly 5 elements")
    if len(l)==6:
        return (l[3]+l[4])/2
    else:
        return float('inf')

# Test code
try:
    print(median([-10, 4, 6, 1000, 10, 20]))
    print(median([-100, 4, 6, 1000, 10, 20]))
    print(median([-10, 4, -20, 1000, 10, 20]))
    print(median([-10, 4, 6, -20, 1000, 10, 20]))
except ValueError as ve:
    print(ve)
```