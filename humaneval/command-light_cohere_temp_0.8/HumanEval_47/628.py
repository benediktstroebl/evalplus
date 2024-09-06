```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
# Test cases
for test_set in [[-10, 4, 6, 1000, 10, 20], [3, 1, 2, 4, 5], [1, 2, 3, 4, 5, 6], [10, -20, -40, -100, -200]]:
    actual_median = median(test_set)
    print(f"Test {test_set}: Expected {test_set[-1]} but got {actual_median}")
```