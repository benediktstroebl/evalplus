```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) < 1:
        raise ValueError("List is empty.
    if len(lst) == 1:
        return lst[0]
    n = len(lst) // 2 + 1
    m = (n + 1) // 2
    for i in range(m):
        if lst[i] > lst[i + n]:
            lst[i], lst[i + n] = lst[i + n], lst[i]
    return lst[m - 1]
# Test cases
try:
    print(median([3, 1, 2, 4, 5]))  # Output: 5.0
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
except ValueError as e:
    print("Error:", e)
```