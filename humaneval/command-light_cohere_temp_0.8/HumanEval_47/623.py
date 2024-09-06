```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) <= 1:
        return l[0]
    m = l[(len(l) + 1) // 2]
    for num in l:
        if num > m:
            m = num
    return m
# pass-tests
print(median([3, 1, 2, 4, 5])) # 3
print(median([-10, 4, 6, 1000, 10, 20])) # 15.0
print(median([10, -5, -8, -3, -1])) # -1
print(median([-1, -10, -100])) # -1
print(median([9, -9, -8, -7, -6])) # -8
```