```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("Input list must have at least two elements.")
    mid = len(l) // 2
    if l[mid] > l[-1]:
        mid += 1
    l.sort()
    small = []
    for i in range(len(l) - 1):
        small.append(l[i])
    small.sort()
    required to have at least odd length
    if len(small) == 1:
        return l[0]
    elif len(small) == 2:
        return (small[0] + small[1]) / 2
    else:
        return median(small)

# Test cases
print(median([-10, 4, 6, 1000, 10, 20]))    # Expected output: 15.0
print(median([10, 20, -10, 40, 30, -20]))    # Expected output: 10
```