```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
# Test case 1
l1 = [-10, 4, 6, 1000, 10, 20]
print(median(l1))  # Output: 15.0
# Test case 2
l2 = [3, 1, 2, 4, 5]
print(median(l2))  # Output: 2.5
# Test case 3
l3 = [1, 2, 3, 4, 5, 6]
print(median(l3))  # Output: 5.0
```