```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Unit tests
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
test_median()()
```
Do you need assistance with anything else?