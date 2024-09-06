```python
def median(l):
    """Return median of elements in the list l."""
    return (sum(map(lambda x: x, l)) + 1) / 2.0
```

def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    ```