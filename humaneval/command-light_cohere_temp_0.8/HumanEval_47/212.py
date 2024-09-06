```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

#Test the function
def testmedian():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([-1, 4, 6, 1000, -100, 20]) == 4.0
    assert median([5, 5, 4, 3, 2, 1]) == 4.0
    assert median([3, 3, 3, 2, 1]) == 3.0

testmedian()
```