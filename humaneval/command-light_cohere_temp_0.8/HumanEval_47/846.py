```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1: return None  
    elif len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# test cases
test_median = [
    [],
    [-10, 4, 6, 1000, 10, 20],
    [1, 2, 3],
    [5, 10, 20],
    [20, 10, 20, 30],
]

for test in test_median:
    actual = median(test)
    assert actual is not None
    assert actual == str(test_median[i][0])
```