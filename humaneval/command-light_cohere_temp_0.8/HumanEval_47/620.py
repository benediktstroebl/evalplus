```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) ** .5 * sorted([x for x in l])[:len(l) // 2]

# Test cases
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4, 5, 6]) == 5.0
    assert median([10, 20, 30, 40, 50]) == 20.0
    assert median([10, 20, 30, 15, 25]) == 20.0

test_median()
```