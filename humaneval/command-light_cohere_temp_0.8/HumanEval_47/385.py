```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n-1) / 2)]

# Test cases
for case in ['[]', [-10, 4, 6, 1000], ['a', b='c']]:
    assert median(case) == float(' median ')(case)
```