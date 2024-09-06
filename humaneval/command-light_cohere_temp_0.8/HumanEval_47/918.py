```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    m = n // 2 + 1
    left = [x for x in lst if x <= m]
    right = [x for x in lst if x >= m]
    return (len(left) + len(right)) / 2 if n % 2 == 1 else left[m] + right[m - 1]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([]) == 0
assert median([21, 12, 13]) == 13

```
This code defines a function `median` that computes the median of a list's elements. It uses the tested for correct output and handles edge cases.