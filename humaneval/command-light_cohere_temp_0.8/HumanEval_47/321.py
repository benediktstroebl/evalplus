```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for i in range(0, 10):
    lst = [i, i+1, i*2, i*3]
    assert median(lst) == i*3

# Test case with negative numbers
lst = [4,-10,6,1000]
assert median(lst) == -6
```