```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
test_median()
```