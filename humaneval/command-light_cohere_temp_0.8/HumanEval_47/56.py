```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test the function
for i in range(0, 10):
    assert median([i, i + 1]) == i + 1  # This should be true!

for i in range(0, 10):
    assert median([-10, -9, -10, -11, -12]) == -11  # This should be true!

for i in range(0, 10):
    assert median([10, 9, 10, 10]) == 10 # This should be true!

for i in range(0, 10):
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0  # This boundaries
for i in range(1, 10):
        assert median([-10-i, -9, -10, -11, -12]) == -11  # This should be true!
```