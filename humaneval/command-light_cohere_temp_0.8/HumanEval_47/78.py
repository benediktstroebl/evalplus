```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("List cannot be empty.")
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle - 1] + l[middle]) / 2
    else:
        return l[middle]

# Test cases
test_median = []
test_median.add([4, 1, 2, 3, 4, 5])
test_median.add([1, 2, 3, 4, 5, 6])
test_median.add([10, 20, 1000])
test_median.add([-10, -5, -20])
test_median.add([1, 2, 3, 4, 5, 6, 7, 8, 9])

for x in test_median:
    print(median(x))
```