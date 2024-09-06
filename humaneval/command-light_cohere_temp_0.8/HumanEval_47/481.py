```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test cases
for _ in range(50):
    lst = [i for i in range(100)]
    assert median(lst) == int(round((lst[len(lst) / 2] + lst[len(lst) // 2]) / 2))
```