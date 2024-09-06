```python
def median(lst):
    """Return the median of the list lst."""
    n = len(lst)
    m = n//2 + 1
    i = 0
    while i < m:
        if lst[i] < lst[m]:
            i += 1
        else:
            j = m - i - 1
            lst[j], lst[i] = lst[i], lst[j]
            m -= 1
            i += 1
    return lst[m]
# Sample Test Cases
print(median([-10, 4, 6, 1000, 10, 20])) # 15.0
print(median([3, 1, 2, 4, 5])) # 5.0
print(median([-10, 4, 6, 1000, 10, 20])) # 15.0
print(median([10, 20, 30, 40, 70, 90])) # 70.0
```
The median function returns the median value of the list. The median value is the middle value of the list when the number of elements is even, and is the average of the two middle numbers when the number of elements is odd.