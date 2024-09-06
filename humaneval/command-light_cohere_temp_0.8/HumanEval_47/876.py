```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l.[n//2][0] + l.[n//2][1]) / 2
    else:
        return l.[n//2][0]

# Test
def testMedian(lst):
    assert median(lst) == (l.[n//2][0] + l.[n//2][1]) / 2

testMedian([-10, 4, 6, 1000, 10, 20])
```