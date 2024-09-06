```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n//2-1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# test
def test():
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0

test()
```