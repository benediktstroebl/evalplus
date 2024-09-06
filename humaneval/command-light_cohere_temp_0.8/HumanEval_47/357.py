```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 15.0
```