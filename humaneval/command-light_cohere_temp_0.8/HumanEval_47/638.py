```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return None
    m = n // 2 + 1
    mid1 = lst[m - 1]
    mid2 = lst[m]
    mid3 = lst[m + 1]
    if all(x <= mid1 for x in lst):
        return mid1
    elif all(x >= mid3 and x <= lst[-1]):
        return mid3
    else:
        return median(lst[m - 1] + lst[m + 1])

# Test the function with provided example
result = median([-10, 4, 6, 1000, 10, 20])
assert result == 15.0
```