```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l![n//2 - 1] + l![n//2]) / 2
    else:
        return lst[n//2]

# Test suite
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```