```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    m = n // 2 + 1
    i = m - 1
    while i >= 0 and l[i] == l[i - 1]:
        i -= 1
    if i == -1:
        return None  # No middle element
    median_val = l[i]
    left_subset = l[:i]
    right_subset = l[i + 1:]
    left_idx = 0
    right_idx = len(left_subset) - 1
    while left_idx < len(left_subset) and right_idx >= 0 and left_subset[left_idx] <= right_subset[right_idx]:
        left_idx += 1
    right_idx -= 1
    if left_idx == len(left_subset):
        return median_val
    median_left = left_subset[left_idx]
    median_right = right_subset[right_idx]
    return median_val
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 15.0
```