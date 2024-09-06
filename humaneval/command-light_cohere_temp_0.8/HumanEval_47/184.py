```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test case 1
for _ in range(5):
    a = [-10, 4, 6, 1000, 10, 20]
    assert median(a) == 15.0

# Test case 2
for _ in range(10):
    b = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    assert median(b) == 5.0

# Test case 3
c = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert median(c) == 5.0

# Test case 4
d = [10, 20, 4, 6, 3, 2, 1, 5]
assert median(d) == 3.0

# Test case 5
e = [10, 20, -10, 4, 6, 3, 2, 5]
assert median(e) == -3.0
```
This Python script defines a function `median` that computes the median of a given list of numbers. The function has a corresponding test cases that verify its functionality, including edge cases and handling lists with odd lengths.