```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2) - 1] + lst[n//2]) / 2
    else:
        return lst[(n//2)]

# Test case 1:
def test1():
    assert median([3, 1, 2, 4, 5]) == 3

# Test case 2:
def test2():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3:
def test3():
    assert median([1, 2, 4, 5, 6]) == 5
```