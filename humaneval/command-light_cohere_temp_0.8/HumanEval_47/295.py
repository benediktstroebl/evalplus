```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function
for _ in range(25):
    lst = [i for i in range(100)]
    assert median(lst) == (lst[50] + lst[49]) / 2
```