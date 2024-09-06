```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function with some values
for _ in range(10):
    test_value = list(_)
    print(median(test_value), end=' ')
```