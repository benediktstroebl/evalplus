```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function
for i in range(0, 10):
    assert median([i, i+1]) == i+1
```