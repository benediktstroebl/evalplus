```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    m = n // 2 + 1
    if n % 2 == 1:
        return (lst[m-1] + lst[m]) / 2
    else:
        return lst[m]

# test case
def test():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test()
```