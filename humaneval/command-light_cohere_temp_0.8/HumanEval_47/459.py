```python
def median(l: list):
    """Return median of elements in the list l."""
    m = len(l) // 2 + 1
    if m % 2 == 0:
        return (l[m//2-1] + l[m//2]) / 2
    else:
        return l[m//2]

# Test case 1
test_median = [4, 2, 3, 1]
assert median(test_median) == 2

# Test case 2
test_median = [10, -10, 4, 6]
assert median(test_median) == 5

# Test case 3
test_median = [1000, 10, 20, 4]
assert median(test_median) == 5

# Test case 4
test_median = [1, 2, 3, 4, 5]
assert median(test_median) == 3
```